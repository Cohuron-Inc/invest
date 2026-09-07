import { readFileSync, existsSync, readdirSync } from 'node:fs'
import { resolve } from 'node:path'
import { connect, rows, repoRoot } from './connect.js'

/** `pnpm q <name> [--symbol NVDA]` - runs queries/<name>.sql. */
async function main(): Promise<void> {
  const name = process.argv[2]
  const dir = resolve(repoRoot, 'queries')
  if (!name) {
    console.log('Saved queries:\n' + readdirSync(dir).filter((f) => f.endsWith('.sql') && !f.startsWith('_'))
      .map((f) => `  ${f.replace(/\.sql$/, '')}`).join('\n'))
    return
  }
  const path = resolve(dir, `${name}.sql`)
  if (!existsSync(path)) throw new Error(`no such query: ${name}`)

  let sql = readFileSync(path, 'utf8')
  // Named params are substituted as quoted literals; values come from the
  // local operator's own argv, never from corpus content.
  for (let i = 3; i < process.argv.length; i += 2) {
    const flag = process.argv[i]
    const value = process.argv[i + 1]
    if (!flag?.startsWith('--') || value === undefined) continue
    sql = sql.replaceAll(`$${flag.slice(2)}`, `'${value.replace(/'/g, "''")}'`)
  }

  const connection = await connect()
  const result = await rows(connection, sql)
  if (result.length === 0) console.log('(no rows)')
  else console.table(result.map((r) => Object.fromEntries(
    Object.entries(r).map(([k, v]) => [k, typeof v === 'bigint' ? Number(v) : v]),
  )))
}

main().catch((err) => { console.error(String(err)); process.exit(1) })
