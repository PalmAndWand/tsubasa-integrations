# ZeroStack

Merge [zerostack.json](../presets/zerostack.json) into your ZeroStack
configuration and set `TSUBASA_API_KEY` through your shell or secret manager.
ZeroStack accepts JSON, YAML and TOML configurations; `ZS_CONFIG_DIR` selects
the configuration directory. See
[ZeroStack's configuration guide](https://github.com/gi-dellav/zerostack/blob/main/docs/CONFIG.md)
for the default path on your platform.

```sh
zerostack --provider tsubasa --model tsubasa-fast --no-tools
```

Use `--model tsubasa-pro` for the other alias. This recipe selects the existing
OpenAI-compatible Chat Completions transport and sends prompts and
`TSUBASA_API_KEY` to `api.tsubasa.sh`.

Keep `context_window: 32768` and `max_tokens: 4096`; prompts, tools and history
must fit alongside the output reservation. The explicit context setting avoids
ZeroStack's 128,000-token fallback when model discovery omits context metadata.

The command above disables tools. When the endpoint and model support tool
calls, a limited read-only setup is `--tools read --read-only` instead of
`--no-tools`. Additional tools and long histories consume context.
