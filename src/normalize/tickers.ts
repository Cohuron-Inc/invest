import type { SymbolRow } from '../lib/config.js'
import type { XTweet } from '../x/types.js'

export type MentionSource = 'cashtag_entity' | 'regex_text' | 'url_resolved' | 'llm'

export type ExtractedMention = {
  symbol: string
  symbol_raw: string
  mention_source: MentionSource
  asset_class: string
  occurrences: number
  first_char_offset: number | null
}

export type Extraction = {
  mentions: ExtractedMention[]
  /** Ticker-shaped strings we could not classify. Never silently dropped: this
   *  is the feedback loop on resolver quality. */
  unresolved: string[]
}

/** `$NVDA`, `$brk.b` - the explicit, self-identifying form. */
const CASHTAG_RE = /\$([A-Za-z][A-Za-z.-]{0,5})\b/g
/** A bare all-caps token. Only trusted when it is in a known universe. */
const BARE_RE = /\b([A-Z]{1,5})\b/g

export type Resolver = {
  symbols: Map<string, SymbolRow>
  /** security_name (upper) -> symbol, for names with no ticker (private cos). */
  names: Map<string, string>
  blocklist: Set<string>
  /** Listed universe: classifies a cashtag as a real security. */
  universe: Set<string>
  /** The only symbols accepted without a leading '$'. */
  bare: Set<string>
}

export function buildResolver(
  symbols: SymbolRow[], blocklist: Set<string>, universe: Set<string>, bare: Set<string> = new Set(),
): Resolver {
  const bySymbol = new Map<string, SymbolRow>()
  const names = new Map<string, string>()
  for (const row of symbols) {
    bySymbol.set(row.symbol, row)
    if (row.security_name) names.set(row.security_name.toUpperCase(), row.symbol)
  }
  return { symbols: bySymbol, names, blocklist, universe, bare }
}

/** Follows a rename (FB -> META) so multi-year analysis stays on one series. */
function canonical(symbol: string, r: Resolver): { symbol: string; asset_class: string } {
  const row = r.symbols.get(symbol)
  if (!row) {
    return { symbol, asset_class: r.universe.has(symbol) ? 'equity' : 'unknown' }
  }
  if (row.alias_of) {
    const target = r.symbols.get(row.alias_of)
    return { symbol: row.alias_of, asset_class: target?.asset_class ?? 'equity' }
  }
  return { symbol: row.symbol, asset_class: row.asset_class || 'unknown' }
}

/** Accepted as a ticker when written bare, without a '$'. */
function acceptsBare(symbol: string, r: Resolver): boolean {
  if (r.blocklist.has(symbol)) return false
  return r.bare.has(symbol) || (r.symbols.has(symbol) && r.symbols.get(symbol)!.asset_class !== 'equity')
}

export function extractMentions(tweet: XTweet, r: Resolver): Extraction {
  const text = tweet.note_tweet?.text ?? tweet.text ?? ''
  type Hit = { symbol: string; raw: string; source: MentionSource; offset: number | null }
  const hits: Hit[] = []
  const unresolved = new Set<string>()

  // Cashtag spans are masked out of the text before bare-token scanning, so
  // "$NVDA" is counted once as a cashtag rather than twice (once as the cashtag
  // and again as the bare token NVDA sitting inside it).
  const masked = text.split('')
  const mask = (from: number, len: number): void => {
    for (let i = from; i < from + len && i < masked.length; i++) masked[i] = ' '
  }

  // 1. Cashtags. Self-identifying: the author explicitly marked this as a
  //    ticker, so it is recorded even when we cannot classify it - an unknown
  //    symbol is data, not noise.
  const seenOffsets = new Set<number>()
  for (const c of tweet.entities?.cashtags ?? []) {
    hits.push({ symbol: canonical(c.tag.toUpperCase(), r).symbol, raw: c.tag, source: 'cashtag_entity', offset: c.start })
    seenOffsets.add(c.start)
    mask(c.start, c.end - c.start)
  }
  // Cashtags the entity parser missed (it skips some punctuation forms).
  for (const m of text.matchAll(CASHTAG_RE)) {
    const offset = m.index ?? 0
    if (seenOffsets.has(offset)) continue
    const raw = m[1]!
    hits.push({ symbol: canonical(raw.toUpperCase(), r).symbol, raw, source: 'regex_text', offset })
    mask(offset, m[0]!.length)
  }

  const rest = masked.join('')

  // 2. Bare uppercase tokens, trusted ONLY against a known universe: "CEO",
  //    "AI" and "ALL" are words far more often than they are tickers.
  for (const m of rest.matchAll(BARE_RE)) {
    const token = m[1]!
    if (r.blocklist.has(token)) continue
    if (acceptsBare(token, r)) {
      hits.push({ symbol: canonical(token, r).symbol, raw: token, source: 'regex_text', offset: m.index ?? null })
    } else if (token.length >= 2 && r.universe.has(token)) {
      // Ticker-shaped and genuinely listed, but not on the bare allowlist. Kept
      // as a candidate so the allowlist can be grown from real evidence.
      unresolved.add(token)
    }
  }

  // 3. Companies with no ticker to match on (private and pre-IPO names).
  const upperRest = rest.toUpperCase()
  for (const [name, symbol] of r.names) {
    if (name.length < 4) continue
    const at = upperRest.indexOf(name)
    if (at === -1) continue
    if (hits.some((h) => h.symbol === symbol)) continue
    hits.push({ symbol, raw: name, source: 'regex_text', offset: at })
  }

  const bySymbol = new Map<string, Hit[]>()
  for (const h of hits) {
    const list = bySymbol.get(h.symbol)
    if (list) list.push(h)
    else bySymbol.set(h.symbol, [h])
  }

  const mentions: ExtractedMention[] = [...bySymbol.entries()]
    .map(([symbol, list]) => {
      // A cashtag is stronger evidence than a bare-token match.
      const cashtag = list.find((h) => h.source === 'cashtag_entity')
      const offsets = list.map((h) => h.offset).filter((o): o is number => o !== null)
      return {
        symbol,
        symbol_raw: (cashtag ?? list[0]!).raw,
        mention_source: (cashtag ? 'cashtag_entity' : list[0]!.source) as MentionSource,
        asset_class: canonical(symbol, r).asset_class,
        occurrences: list.length,
        first_char_offset: offsets.length ? Math.min(...offsets) : null,
      }
    })
    .sort((x, y) => x.symbol.localeCompare(y.symbol))

  for (const m of mentions) unresolved.delete(m.symbol)
  return { mentions, unresolved: [...unresolved].sort() }
}

/** A retweet is an echo, not a call - materialised here so attribution queries
 *  never have to re-derive it. */
export function postType(tweet: XTweet): 'original' | 'reply' | 'quote' | 'retweet' {
  const refs = tweet.referenced_tweets ?? []
  if (refs.some((r) => r.type === 'retweeted')) return 'retweet'
  if (refs.some((r) => r.type === 'quoted')) return 'quote'
  if (refs.some((r) => r.type === 'replied_to')) return 'reply'
  return 'original'
}
