# Dexto

Use the existing `openai-compatible` provider. In your agent YAML, replace the
`llm` section with:

```yaml
llm:
  provider: openai-compatible
  model: tsubasa-fast
  baseURL: https://api.tsubasa.sh/v1
  apiKey: $TSUBASA_API_KEY
  maxInputTokens: 24576
  maxOutputTokens: 8192
  allowedMediaTypes: []
```

Set `TSUBASA_API_KEY`, then start your agent:

```sh
: "${TSUBASA_API_KEY:?Set TSUBASA_API_KEY}"
dexto --agent /path/to/your-agent.yml
```

The key reference expands when Dexto loads the configuration. The guard prevents
starting with a missing Tsubasa key. To use Pro, change `model` to
`tsubasa-pro`. Both aliases have a 32,768-token context limit; this
configuration reserves 8,192 tokens for output and 24,576 for input. Media input
is disabled.

Controlled checks used `@dexto/core` 1.12.1: this YAML passed the native configuration schema and production `createVercelModel` factory, and both aliases decoded JSON and streamed text through the real SDK. An invalid key produced HTTP 401; the shell guard stopped missing-key dispatch. All five captured requests passed the Tsubasa schema and context checks. The complete CLI agent, UI, and live inference remain unqualified.
