import { DuckDBInstance } from '@duckdb/node-api'
import { dataRoot } from '../duck/connect.js'

/**
 * The capture cursor is derived from the RAW layer, never from a mutable state
 * file and never from the normalized layer.
 *
 * Not a state file, because it would be the only path two runs both rewrite -
 * the sole source of rebase conflicts - and a cursor committed out of sync with
 * the data either re-reads (costing money) or skips posts (losing them
 * permanently).
 *
 * Not the normalized layer, because normalize can lag or fail while capture has
 * already committed. Deriving from `posts` would then re-read - and re-pay for -
 * everything captured but not yet normalized.
 *
 * Post ids are snowflakes, so the numeric maximum is the newest post we hold.
 */
export async function readCursor(root = dataRoot()): Promise<string | null> {
  const instance = await DuckDBInstance.create()
  const connection = await instance.connect()
  try {
    const result = await connection.runAndReadAll(
      `SELECT max(CAST(id AS UBIGINT))::VARCHAR AS cursor
         FROM read_json_auto('${root}/raw/*/*.jsonl.gz', union_by_name => true, ignore_errors => true)`,
    )
    const value = result.getRowObjects()[0]?.['cursor']
    return value == null ? null : String(value)
  } catch (err) {
    // No raw files yet is the expected cold-start case, not a failure.
    if (/No files found|IO Error/i.test(String(err))) return null
    throw err
  }
}
