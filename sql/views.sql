-- The ONLY sanctioned read path for the corpus.
--
-- Two rules this file exists to enforce:
--   1. Partitions are keyed by ingest_dt (CAPTURE date), never by post creation
--      date. search/recent reaches back 7 days, so a post created on the 1st can
--      be captured on the 6th. Keying on creation date would force rewrites of
--      old partitions; keying on capture date keeps every file immutable.
--   2. Because of (1), and because a retry writes a new run-scoped file rather
--      than overwriting, THE SAME post_id APPEARS IN MORE THAN ONE FILE.
--      Never read the parquet directly. Always read through these views.

CREATE OR REPLACE VIEW posts_v AS
SELECT * FROM read_parquet('{{DATA}}/posts/*/*.parquet',
                           hive_partitioning => true, union_by_name => true)
QUALIFY row_number() OVER (PARTITION BY post_id ORDER BY ingest_dt, ingested_at) = 1;

CREATE OR REPLACE VIEW mentions_v AS
SELECT * FROM read_parquet('{{DATA}}/mentions/*/*.parquet',
                           hive_partitioning => true, union_by_name => true)
QUALIFY row_number() OVER (PARTITION BY mention_id ORDER BY ingest_dt) = 1;

CREATE OR REPLACE VIEW picks_v AS
SELECT * FROM read_parquet('{{DATA}}/picks/*/*.parquet',
                           hive_partitioning => true, union_by_name => true);

CREATE OR REPLACE VIEW pick_tags_v AS
SELECT * FROM read_parquet('{{DATA}}/pick_tags/*/*.parquet',
                           hive_partitioning => true, union_by_name => true);

-- Adjusted closes change retroactively after splits/dividends, so the price
-- layer is append-only and we take the most recent observation of each bar.
CREATE OR REPLACE VIEW prices_v AS
SELECT * FROM read_parquet('{{DATA}}/prices/*/*.parquet',
                           hive_partitioning => true, union_by_name => true)
QUALIFY row_number() OVER (
  PARTITION BY symbol, trade_date, price_source ORDER BY ingest_dt DESC
) = 1;

-- ---------------------------------------------------------------------------
-- Attribution lane: who actually said something first.
-- ---------------------------------------------------------------------------

-- A retweet is an echo, not a call. Including retweets makes any lead/lag
-- leaderboard meaningless. LLM-inferred mentions are excluded too: they are
-- useful for narrative but must not earn first-mover credit.
CREATE OR REPLACE VIEW mention_events AS
SELECT symbol, author_id, author_username, post_id, created_at
FROM mentions_v
WHERE post_type <> 'retweet'
  AND mention_source IN ('cashtag_entity', 'regex_text', 'url_resolved');

-- Sessionize into episodes. Without this, "lag vs. the first mention" is
-- measured against a single mention from months ago and every number after
-- week one is meaningless. A gap > 7 days on a symbol starts a new episode.
CREATE OR REPLACE VIEW mention_episodes AS
WITH gapped AS (
  SELECT *,
         CASE WHEN LAG(created_at) OVER w IS NULL
                OR created_at - LAG(created_at) OVER w > INTERVAL 7 DAY
              THEN 1 ELSE 0 END AS is_episode_start
  FROM mention_events
  WINDOW w AS (PARTITION BY symbol ORDER BY created_at, post_id)
)
SELECT *,
       SUM(is_episode_start) OVER (PARTITION BY symbol ORDER BY created_at, post_id
                                   ROWS UNBOUNDED PRECEDING) AS episode_no
FROM gapped;

CREATE OR REPLACE VIEW author_episode_entry AS
WITH per_author AS (
  SELECT symbol, episode_no, author_id, author_username,
         MIN(created_at)              AS author_first_at,
         ARG_MIN(post_id, created_at) AS author_first_post_id
  FROM mention_episodes
  GROUP BY 1, 2, 3, 4
)
SELECT *,
       MIN(author_first_at) OVER (PARTITION BY symbol, episode_no) AS episode_first_at,
       COUNT(*)             OVER (PARTITION BY symbol, episode_no) AS episode_n_authors
FROM per_author;
