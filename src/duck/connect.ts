import { DuckDBInstance, type DuckDBConnection } from '@duckdb/node-api'
import { readFileSync } from 'node:fs'
import { fileURLToPath } from 'node:url'
import { dirname, resolve } from 'node:path'

const here = dirname(fileURLToPath(import.meta.url))
export const repoRoot = resolve(here, '../..')

/**
 * The data root is parameterised rather than hardcoded so the identical view
 * definitions run against the working tree, a test fixture, or remote object
 * storage. DuckDB reads `s3://` and `r2://` natively, so outgrowing git is a
 * change to one environment variable - not a migration.
 */
export function dataRoot(): string {
  return process.env.INVEST_DATA_ROOT ?? resolve(repoRoot, 'data')
}

export function refRoot(): string {
  return process.env.INVEST_REF_ROOT ?? resolve(repoRoot, 'ref')
}

/** Renders sql/views.sql against the active roots. */
export function renderViews(data = dataRoot(), ref = refRoot()): string {
  return readFileSync(resolve(repoRoot, 'sql/views.sql'), 'utf8')
    .replaceAll('{{DATA}}', data)
    .replaceAll('{{REF}}', ref)
}

/** Opens an in-process DuckDB with every corpus view already created. */
export async function connect(
  opts: { data?: string; ref?: string } = {},
): Promise<DuckDBConnection> {
  const instance = await DuckDBInstance.create()
  const connection = await instance.connect()
  await connection.run(renderViews(opts.data ?? dataRoot(), opts.ref ?? refRoot()))
  return connection
}

export async function rows(
  connection: DuckDBConnection,
  sql: string,
): Promise<Record<string, unknown>[]> {
  return (await connection.runAndReadAll(sql)).getRowObjects()
}
