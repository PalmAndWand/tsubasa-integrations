# Agentty

Use Tsubasa through Agentty's custom OpenAI-compatible endpoint and its
read-only `explorer` role:

```sh
: "${TSUBASA_API_KEY:?Set TSUBASA_API_KEY}"
OPENAI_API_KEY="$TSUBASA_API_KEY" \
AGENTTY_MAX_CONTEXT_TOKENS=32768 \
AGENTTY_MAX_OUTPUT_TOKENS=8192 \
agentty run "Explain the relevant files without changing them." \
  --provider https://api.tsubasa.sh/v1 --model tsubasa-fast --agent explorer
```

Use `--model tsubasa-pro` for Pro. The key assignment applies only to this
command because Agentty's custom endpoint reads `OPENAI_API_KEY`; Agentty does
not automatically read `TSUBASA_API_KEY`.

This recipe uses the smaller read-only toolset. It does not cover the default
`general` role or a long interactive session. Both aliases have a 32,768-token
context window; the 8,192-token output reservation leaves room for the prompt.

Checked with the official Agentty v0.9.13 macOS ARM64 binary: both aliases
decoded a controlled SSE response, an invalid dedicated key caused HTTP 401 and
a CLI failure, and the missing-key guard stopped before HTTP. All three actual
requests passed the API schema and context checks. No model tool execution or
live inference was qualified.
