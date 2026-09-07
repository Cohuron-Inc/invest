import type { ResolvedAccount } from '../lib/config.js'

/**
 * X recent-search caps the query at 512 characters on the pay-per-use and
 * legacy Basic tiers. All 12 handles fit in one `from:` disjunction (~270
 * chars), which is why capture is one request with one cursor rather than
 * twelve. If the allowlist ever grows past the cap, build() splits it into the
 * fewest possible chunks rather than silently truncating.
 */
export const QUERY_CHAR_LIMIT = 512

export function buildQueries(accounts: ResolvedAccount[], limit = QUERY_CHAR_LIMIT): string[] {
  if (accounts.length === 0) throw new Error('refusing to build a query for an empty allowlist')

  const terms = accounts.map((a) => `from:${a.handle}`)
  const queries: string[] = []
  let current: string[] = []

  for (const term of terms) {
    const candidate = [...current, term].join(' OR ')
    if (candidate.length > limit) {
      if (current.length === 0) {
        throw new Error(`single term exceeds the ${limit}-char query limit: ${term}`)
      }
      queries.push(current.join(' OR '))
      current = [term]
    } else {
      current.push(term)
    }
  }
  if (current.length > 0) queries.push(current.join(' OR '))
  return queries
}
