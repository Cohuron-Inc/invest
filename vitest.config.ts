import { defineConfig } from 'vitest/config'

export default defineConfig({
  test: {
    // Match the house convention: `vitest` and `vitest run` behave identically,
    // so CI never hangs waiting on a watcher.
    watch: false,
    include: ['src/**/*.{test,spec}.ts'],
    // The ET trading-day boundary must not depend on the runner's clock.
    env: { TZ: 'UTC' },
  },
})
