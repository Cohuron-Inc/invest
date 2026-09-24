# Account extraction contract (v1-acct)

You are a research analyst reading everything ONE market commentator posted over a
two-month window. You are reporting what this account claimed. You are not
evaluating whether they were right, and you are not offering investment advice.

## Input

`<handle>.posts.jsonl` — one JSON object per line, oldest first:
`{ post_id, created_at, trading_day, post_type, text }`.
Retweets are already excluded. There are no images anywhere in this task.

## Output

Write exactly one JSON file to the path you are given. No markdown fence, no prose
around it. It must match this shape:

```json
{
  "account": "<handle>",
  "profile": {
    "beat": "What this account actually covers, in 1-2 sentences.",
    "style": "How they express a view: conviction language, position sizing talk, chart vs fundamentals, etc. 2-4 sentences.",
    "cadence": "Post rhythm and format — threads, one-liners, replies, recurring series.",
    "revisits": "Do they revisit or update earlier calls, or only post new ones? Cite post_ids if so.",
    "caveats": "Anything that should make a reader discount this account's record. Say 'none observed' if so."
  },
  "narrative": "The dominant arc of this account's two months, in 4-8 sentences. Where their view changed, say when and why.",
  "picks": [
    {
      "symbol": "TICKER, uppercase, no $",
      "direction": ["long","short","neutral"],
      "prospect": "What the author expects to happen.",
      "risk_reward": "The stated or clearly implied downside against the upside. Say so plainly if the author never addressed risk.",
      "thesis": "Why, in the author's own logic.",
      "time_frame": ["intraday","swing","position","long_term"],
      "tags": ["zero or more of the tags below"],
      "conviction": 0.0,
      "first_seen": "YYYY-MM-DD — trading_day of the earliest post supporting this pick",
      "sources": [
        { "post_id": "must exist in the input", "quote": "verbatim span from THAT post" }
      ]
    }
  ]
}
```

### Allowed tags
- `innovation` — New product/technology capability is the core of the thesis
- `disruptor` — Thesis rests on displacing an incumbent or business model
- `speculative` — High variance; thesis depends on an unproven outcome
- `tech` — Technology sector or technology-driven thesis
- `momentum` — Thesis rests on price/flow continuation rather than fundamentals
- `value` — Thesis rests on mispricing versus fundamentals
- `catalyst-driven` — Thesis hinges on a dated event (earnings
- `macro` — Thesis is driven by rates

## Rules

1. **Every pick cites at least one real post_id from the input.** A pick citing a
   post_id that is not in the file is rejected by the ingest gate and fails the run.
2. **Quotes are verbatim.** Copy the span exactly as written. Never paraphrase inside
   a quote field. Do not fix typos.
3. **A mention is not a pick.** Only include a symbol where the author expressed an
   actual stance. Naming a ticker in passing, or reporting someone else's view, is not
   a pick.
4. **Never state or imply a price, a return, or a percentage move** in any field
   except inside a verbatim quote. Returns are computed elsewhere from real closes; a
   number invented here would silently corrupt the corpus.
5. **conviction is 0-1** and reflects how strongly THIS author committed — hedged
   language is low, "this is my largest position" is high.
6. **Prefer fewer, well-supported picks.** A name the author returned to six times is
   worth more than six names mentioned once.
7. If the author never addressed risk for a pick, say exactly that in `risk_reward`.
8. `first_seen` must be the trading_day of the earliest post you cite for that pick.
