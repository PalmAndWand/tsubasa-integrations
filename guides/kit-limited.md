# Tsubasa in KIT

Use [kit-limited.yaml](../presets/kit-limited.yaml) with
[KIT](https://github.com/mark3labs/kit) for a short headless text turn.
The named provider uses KIT's existing `openai-compat` transport. Keep that
wire value: `openai` selects the Responses API instead of Chat Completions.

Set `TSUBASA_API_KEY` with your normal secret-management method, then run from
the directory containing the downloaded preset:

```sh
kit --config "$PWD/kit-limited.yaml" \
  --model tsubasa/tsubasa-pro --json 'Reply briefly with a greeting.'
```

Use `tsubasa/tsubasa-fast` for Fast. KIT reads the key through the provider's
`apiKeyEnv` setting and sends the key and prompt to `api.tsubasa.sh`. The preset
caps output at 2,048 tokens and the agent at one step. It disables core tools,
extensions, skills, named agent discovery, prompt templates, and session
persistence. Keep this profile separate from a configuration that adds MCP
servers or extensions.

KIT's named provider override accepts model aliases that are absent from its
model catalog. It does not set per-model context metadata. This profile is
therefore limited to a short turn; it does not establish correct long-session
compaction. Tsubasa enforces a combined 32,768-token input/output limit. A larger
prompt or project context can exceed the remaining budget.

Verification used a build from
[`3d4c7d89d951a0df4f2284480adf70cdcdac7937`](https://github.com/mark3labs/kit/tree/3d4c7d89d951a0df4f2284480adf70cdcdac7937)
with Go 1.27.1. The native CLI decoded streamed text and showed invalid-key
errors on both aliases, using no tool schemas. `--stream=false` still sent SSE
in this build; it is not a JSON transport selector. A separate check loaded the
same provider override and exercised the native provider's `Generate` and
`Stream` methods, including response usage and HTTP 401 status handling.

All 16 captured requests passed the real Tsubasa request schema and context
check before the loopback fixture replied. CLI input was estimated at 1,458
tokens plus 2,048 reserved output. The fixture used synthetic keys, native
configuration, an inherited HOME, and sandbox restrictions on personal files
and external network. It did not edit request bodies.

Live inference, the interactive UI, tools, session resume, and long-session
behavior have not been qualified.
