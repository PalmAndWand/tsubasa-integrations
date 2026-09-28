# Tsubasa in Mistral Vibe

Use [mistral-vibe-read-only.toml](../presets/mistral-vibe-read-only.toml) with
[Mistral Vibe](https://github.com/mistralai/mistral-vibe). This adds custom named
models through its existing generic OpenAI-style backend. Tsubasa is not a stock
Vibe provider. The profile exposes only Vibe's `read_file` tool and uses its
legacy Python harness.

Install Mistral Vibe `2.25.8` using its official instructions. From the directory
containing the downloaded preset, create a dedicated profile:

```sh
export VIBE_HOME="$PWD/.vibe-tsubasa"
mkdir -p "$VIBE_HOME"
cp mistral-vibe-read-only.toml "$VIBE_HOME/config.toml"
```

Set `TSUBASA_API_KEY` in your environment using your normal secret-management
method. Run a short turn from a directory you intend Vibe to trust and access:

```sh
VIBE_ACTIVE_MODEL=tsubasa-pro vibe --legacy-harness \
  --prompt 'Reply briefly with a greeting.' --max-turns 1 --trust
```

Use `VIBE_ACTIVE_MODEL=tsubasa-fast` for Fast. This profile disables skills,
connectors, telemetry, update checks, images, and reasoning controls. Both model
entries set auto-compaction at 24,000 tokens for the 32,768-token Tsubasa context.
That threshold does not prove that arbitrary project context or long histories
fit the window.

Do not replace the tool selection with `disabled_tools = ["*"]` in this version.
The legacy CLI then sends `tool_choice: "auto"` without any `tools`, which fails
Tsubasa's request validation. The read-only profile supplies the native tool
definition without modifying the HTTP request. No `read_file` invocation was
executed during validation, so this does not qualify live model tool behavior.

Verification used an isolated profile and a loopback fixture with synthetic
keys. Eight direct generic-backend calls covered both aliases, JSON, streaming,
usage, and invalid-key errors. Two additional native CLI turns loaded the TOML
and streamed the fixture response using the stock prompt and `read_file`
definition. All ten requests passed Tsubasa's real schema and budget check.
The CLI requests used at most 11,694 estimated input tokens and omitted an output
cap, receiving Tsubasa's default 512-token budget. Vibe's `--max-tokens` controls
cumulative session usage; it is not a per-response output cap.

The qualification profile preserved the real `HOME`, blocked personal config
and skill directories, and used separate native config/cache directories. Live
inference, the interactive UI, the experimental harness, file-tool execution,
and long-session compaction have not been verified. The tested `2.25.8` release
corresponds to source `7c19608af06f6c61d63f8f7a5c3430da73fba2ab`.
