# Tsubasa in MiMo Code

Use [mimo-code.json](../presets/mimo-code.json) with
[MiMo Code](https://github.com/XiaomiMiMo/MiMo-Code). This adds a custom provider
using the client's existing `@ai-sdk/openai-compatible` backend. It does not add
Tsubasa to MiMo Code's stock model catalog.

Install the official client; validation used the macOS ARM64
[v0.1.14 release](https://github.com/XiaomiMiMo/MiMo-Code/releases/tag/v0.1.14).
From the directory containing the downloaded preset, create a dedicated profile:

```sh
export MIMOCODE_HOME="$PWD/.mimo-tsubasa"
mkdir -p "$MIMOCODE_HOME"
cp mimo-code.json "$MIMOCODE_HOME/tsubasa.json"
export MIMOCODE_CONFIG="$MIMOCODE_HOME/tsubasa.json"
printf '{}\n' > "$MIMOCODE_HOME/models.json"
export MIMOCODE_MODELS_PATH="$MIMOCODE_HOME/models.json"
export MIMOCODE_DISABLE_AUTOUPDATE=1
export MIMOCODE_ENABLE_ANALYSIS=false
export MIMOCODE_DISABLE_CLAUDE_CODE=1
export MIMOCODE_DISABLE_AGENTS_SKILLS=1
```

Set `TSUBASA_API_KEY` in your environment using your normal secret-management
method. The preset reads that variable instead of storing your key in JSON.
List the named models, then run a short text turn:

```sh
mimo models tsubasa
mimo run --pure --format json --model tsubasa/tsubasa-pro \
  'Reply briefly with a greeting.'
```

Use `--model tsubasa/tsubasa-fast` for Fast. The preset disables tools and tool
permissions, selects only the configured Tsubasa models, declares a 32,768-token
context, and caps each response at 4,096 tokens. The compaction working budget is 24,000 tokens; the default 0.9 ratio
triggers compaction at 21,600 tokens (displayed as 22K). Sustained conversations
and compaction were not tested.

Verification used an isolated profile and a loopback fixture with synthetic
keys, plus an empty local model catalog to avoid unrelated catalog downloads.
Native model listing and four CLI turns covered both aliases, streamed text,
and invalid-key errors. All four serialized requests passed Tsubasa's real
request schema and context-budget check. The stock prompt was estimated at
26,150 input tokens plus 4,096 output tokens, leaving 2,522 tokens in the context
window. Extra project instructions or conversation history can exhaust that
remaining budget. This is Tsubasa's admission estimate, not a universal
tokenizer count.

Live inference, the interactive UI, tools, and long-session behavior have not
been verified. The tested release is pinned to
`2a0eb706e95a77cba34a319e9f11f33f26d4450c`; the separately inspected main source
was `454521a8527686a4132c6dda2d2ff62607dcb892`.
