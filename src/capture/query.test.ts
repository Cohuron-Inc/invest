import { describe, it, expect } from 'vitest'
import { buildQueries, QUERY_CHAR_LIMIT } from './query.js'
import { loadAccounts } from '../lib/config.js'

describe('buildQueries', () => {
  it('fits the real 12-account allowlist in a single query', () => {
    const accounts = loadAccounts().map((a) => ({ handle: a.handle, user_id: a.user_id ?? 'x' }))
    const queries = buildQueries(accounts)
    expect(queries).toHaveLength(1)
    expect(queries[0]!.length).toBeLessThan(QUERY_CHAR_LIMIT)
    for (const a of accounts) expect(queries[0]).toContain(`from:${a.handle}`)
  })

  it('splits rather than truncating when the allowlist outgrows the limit', () => {
    const many = Array.from({ length: 60 }, (_, i) => ({ handle: `account_number_${i}`, user_id: `${i}` }))
    const queries = buildQueries(many)
    expect(queries.length).toBeGreaterThan(1)
    for (const q of queries) expect(q.length).toBeLessThanOrEqual(QUERY_CHAR_LIMIT)
    // nothing is dropped
    const rebuilt = queries.join(' OR ').split(' OR ').sort()
    expect(rebuilt).toHaveLength(60)
  })

  it('refuses an empty allowlist instead of querying for everything', () => {
    expect(() => buildQueries([])).toThrow(/empty allowlist/)
  })
})
