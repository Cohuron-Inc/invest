import { log } from '../lib/log.js'
import type { XSearchPage, XUser, XTweet } from './types.js'

const API = 'https://api.x.com/2'

const TWEET_FIELDS = [
  'id', 'text', 'created_at', 'author_id', 'lang', 'conversation_id',
  'in_reply_to_user_id', 'public_metrics', 'entities', 'referenced_tweets',
  'note_tweet', 'attachments',
].join(',')

export class XApiError extends Error {
  constructor(message: string, readonly status: number, readonly body: string) {
    super(message)
    this.name = 'XApiError'
  }
}

export class XClient {
  private readonly token: string
  /** Posts returned across this client's lifetime - the metered quantity. */
  postsRead = 0

  constructor(token: string) {
    this.token = token
  }

  private async get(path: string, params: Record<string, string>): Promise<unknown> {
    const url = new URL(`${API}${path}`)
    for (const [k, v] of Object.entries(params)) url.searchParams.set(k, v)

    // Retry only what is retryable: 429 and 5xx. A 400 means the query is
    // wrong and retrying just burns time.
    const maxAttempts = 5
    for (let attempt = 1; attempt <= maxAttempts; attempt++) {
      const res = await fetch(url, {
        headers: { authorization: `Bearer ${this.token}`, 'user-agent': 'cohuron-invest/0.1' },
      })
      if (res.ok) return res.json()

      const body = await res.text()
      const retryable = res.status === 429 || res.status >= 500
      if (!retryable || attempt === maxAttempts) {
        throw new XApiError(`X API ${res.status} on ${path}`, res.status, body.slice(0, 500))
      }
      // Honour Retry-After when present; otherwise exponential backoff.
      const header = res.headers.get('retry-after')
      const waitMs = header ? Number(header) * 1000 : Math.min(60_000, 2 ** attempt * 1000)
      log.warn('x.retry', { path, status: res.status, attempt, waitMs })
      await new Promise((r) => setTimeout(r, waitMs))
    }
    throw new Error('unreachable')
  }

  /** Resolve handles to immutable numeric ids. Max 100 per call. */
  async usersByUsername(handles: string[]): Promise<XUser[]> {
    const out: XUser[] = []
    for (let i = 0; i < handles.length; i += 100) {
      const batch = handles.slice(i, i + 100)
      const json = (await this.get('/users/by', {
        usernames: batch.join(','),
        'user.fields': 'username,name',
      })) as { data?: XUser[]; errors?: { detail?: string; value?: string }[] }
      for (const e of json.errors ?? []) {
        log.warn('x.user_unresolved', { detail: e.detail, value: e.value })
      }
      out.push(...(json.data ?? []))
    }
    return out
  }

  /**
   * Page through recent search to exhaustion.
   *
   * `sinceId` is the cost control: it is the difference between reading only
   * what is new and paying again for everything in the window.
   */
  async *searchRecent(opts: {
    query: string
    sinceId?: string | undefined
    startTime?: string | undefined
    maxPages?: number
  }): AsyncGenerator<{ page: XSearchPage; tweets: XTweet[]; users: Map<string, string>; pageNo: number }> {
    let nextToken: string | undefined
    let pageNo = 0
    const maxPages = opts.maxPages ?? 200

    do {
      pageNo++
      const params: Record<string, string> = {
        query: opts.query,
        max_results: '100',
        'tweet.fields': TWEET_FIELDS,
        expansions: 'author_id',
        'user.fields': 'username,name',
      }
      // since_id and start_time are mutually exclusive in practice; since_id
      // wins because it is the one that avoids re-reading (and re-paying).
      if (opts.sinceId) params['since_id'] = opts.sinceId
      else if (opts.startTime) params['start_time'] = opts.startTime
      if (nextToken) params['next_token'] = nextToken

      const page = (await this.get('/tweets/search/recent', params)) as XSearchPage
      for (const e of page.errors ?? []) log.warn('x.partial_error', { title: e.title, detail: e.detail })

      const tweets = page.data ?? []
      this.postsRead += tweets.length
      const users = new Map<string, string>()
      for (const u of page.includes?.users ?? []) users.set(u.id, u.username)

      yield { page, tweets, users, pageNo }
      nextToken = page.meta?.next_token

      if (pageNo >= maxPages && nextToken) {
        log.warn('x.max_pages_reached', { pageNo, postsRead: this.postsRead })
        break
      }
    } while (nextToken)
  }
}

/** ~$0.005 per post read, per X pay-per-use. Verify against the console. */
export const USD_PER_POST_READ = 0.005

export function estimateCostUsd(postsRead: number): number {
  return Number((postsRead * USD_PER_POST_READ).toFixed(4))
}
