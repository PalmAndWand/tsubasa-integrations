# Reasonix

Use Reasonix's custom OpenAI-compatible provider with Tsubasa.

In the desktop app, open **Settings → Model → Access → Add model service →
Custom provider**. Choose the OpenAI-compatible chat protocol, set the API
address to `https://api.tsubasa.sh/v1`, and leave **Full URL** off. Use
`TSUBASA_API_KEY` as the credential variable. Add `tsubasa-fast` and
`tsubasa-pro` to the model list, set the context window to `32768`, and choose
**Plain chat** capability mode.

For the CLI, add this provider entry to the existing `config.toml` in
[Reasonix home](https://github.com/esengine/DeepSeek-Reasonix/blob/studio/docs/CONFIG_PATHS.md).
Preserve the other entries in that file.

```toml
[[providers]]
name = "tsubasa"
kind = "openai"
base_url = "https://api.tsubasa.sh/v1"
models = ["tsubasa-fast", "tsubasa-pro"]
default = "tsubasa-fast"
api_key_env = "TSUBASA_API_KEY"
context_window = 32768
max_output_tokens = 512
reasoning_protocol = "none"
```

Set `TSUBASA_API_KEY` in the environment or use Reasonix's credential store;
keep the secret value out of `config.toml`. Select either model explicitly:

```sh
reasonix --model tsubasa/tsubasa-fast
reasonix --model tsubasa/tsubasa-pro
```

The example reserves 512 output tokens. Both models have a 32,768-token context
window; Fast allows up to 8,192 output tokens and Pro up to 16,384. Leave room
for the prompt when increasing the output budget.

This adds an editable custom provider. It does not add Tsubasa to Reasonix's
curated provider presets.

The native configuration, credential and model loaders passed four controlled
HTTP/SSE requests across both aliases, including rejected-key handling without
fallback to an unrelated key. This verifies the provider runtime; the full
desktop UI, agent prompt and live inference remain unqualified.
