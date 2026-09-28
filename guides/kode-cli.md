# Kode CLI

Use Tsubasa for text-only print requests through Kode's existing custom OpenAI
provider. Complete Kode's first-run setup, then save this as
`tsubasa-models.yaml`:

```yaml
version: 1
profiles:
  - name: Tsubasa Fast
    provider: custom-openai
    modelName: tsubasa-fast
    baseURL: https://api.tsubasa.sh/v1
    apiKey:
      fromEnv: TSUBASA_API_KEY
    contextLength: 32768
    maxTokens: 8192
  - name: Tsubasa Pro
    provider: custom-openai
    modelName: tsubasa-pro
    baseURL: https://api.tsubasa.sh/v1
    apiKey:
      fromEnv: TSUBASA_API_KEY
    contextLength: 32768
    maxTokens: 8192
```

Set `TSUBASA_API_KEY`, then import and select a model:

```sh
: "${TSUBASA_API_KEY:?Set TSUBASA_API_KEY}"
kode models import tsubasa-models.yaml
kode --model tsubasa-fast --safe --output-format json --tools "" \
  --system-prompt "You are a helpful assistant." \
  --strict-mcp-config --mcp-config '{}' --no-session-persistence -p "Say Hello."
```

The empty tool list and short system prompt keep this recipe limited to text
requests. Use `--model tsubasa-pro` for Pro. The JSON print mode forwards the
selected model explicitly. This recipe does not cover the stock coding-agent
prompt or interactive mode.

The import resolves the environment reference and saves the key in Kode's local
configuration; the YAML itself contains no key value. Reimport after rotating
your key. Both models have a 32,768-token context window. The output reservation
is 8,192 tokens for either profile so input has room in that shared window.

Checked with the published `@shareai-lab/kode` 2.2.1 CLI: the imported profiles
selected both aliases and decoded controlled SSE responses. All seven actual
requests passed API schema and context checks. The missing-key guard stopped
before HTTP; invalid-key requests received 401 with no fallback to an unrelated
OpenAI key. The invalid-key process was stopped after ten seconds in Kode's
retry loop, so a clean authentication-error exit was not established. No model
tool execution or live inference was qualified.
