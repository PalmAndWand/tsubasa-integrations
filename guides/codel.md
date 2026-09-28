# CODEL native provider configuration

Apply [the existing environment settings](../presets/codel.env) to CODEL's backend
process. Supply the credential separately, using CODEL's exact `OPEN_AI_KEY` name:

```sh
export OPEN_AI_KEY="${TSUBASA_API_KEY:?Set TSUBASA_API_KEY}"
export OPEN_AI_MODEL=tsubasa-fast
export OPEN_AI_SERVER_URL=https://api.tsubasa.sh/v1
```

Use `OPEN_AI_MODEL=tsubasa-pro` for Pro and select the existing OpenAI provider in
CODEL. Set `TSUBASA_API_KEY` first; the shell check prevents silent use of an
unrelated provider key. These are backend process variables. For a containerized
installation, pass them through its normal environment configuration.

The source pinned at `fe1e846c9e04f41209498ed0d88e92b15dcdfad2` uses the existing
langchaingo 0.1.8 OpenAI transport. Its actual provider factory and `Summary`,
`DockerImageName` and `NextTask` methods were exercised against a controlled HTTP
endpoint for both aliases. Fourteen serialized requests passed the real Tsubasa
schema and context check, including five native tool schemas and a tool-result
history request. Controlled tool calls were decoded into task records; no tool
was executed. Invalid keys surfaced as errors in the text helpers and CODEL's
native ask-user fallback in `NextTask`. The credential guard stopped missing-key
calls before HTTP.

CODEL omits `max_tokens`; Tsubasa selected its 512-token default output reserve.
The largest tested request used 9,520 estimated input tokens plus that reserve.
CODEL's own 30,000-character prompt check does not account for the whole serialized
history and tools, so it cannot guarantee the 32,768-token combined limit. Keep
tasks and histories short.

This is qualification of the native provider methods and request plumbing. The
Docker/task database workflow, browser UI, actual tool execution, long tasks and
live model behavior remain unqualified. The configured provider sends prompts
and `OPEN_AI_KEY` to `https://api.tsubasa.sh/v1`.

Sources: [native provider](https://github.com/semanser/codel/blob/fe1e846c9e04f41209498ed0d88e92b15dcdfad2/backend/providers/openai.go),
[configuration names](https://github.com/semanser/codel/blob/fe1e846c9e04f41209498ed0d88e92b15dcdfad2/backend/config/config.go).
