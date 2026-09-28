# Little Coder

Install Little Coder and set `TSUBASA_API_KEY` through your shell or secret
manager. From this catalog checkout, select the supplied provider configuration:

```sh
LITTLE_CODER_MODELS_FILE="$PWD/presets/little-coder.json" \
  little-coder --model tsubasa/tsubasa-fast --thinking off --no-tools
```

Use `tsubasa/tsubasa-pro` for the other alias. To keep your other custom
providers, merge the `tsubasa` block from
[little-coder.json](../presets/little-coder.json) into your existing Little
Coder `models.json` instead. Its usual location is
`$XDG_CONFIG_HOME/little-coder/models.json` or
`~/.config/little-coder/models.json`; a provider block replaces the same
provider from the shipped configuration.

This recipe uses Little Coder's native Pi Chat Completions transport.
Compatibility flags are repeated on each model because Little Coder's
registration path does not pass through provider-level compatibility flags.
Prompts and `TSUBASA_API_KEY` are sent to `api.tsubasa.sh`.

Both aliases have a 32,768-token context; maximum output is 8,192 for Fast and
16,384 for Pro. Input, tool definitions and output must fit together. The
command above disables tools. Enable tools only when the selected endpoint and
model support them; a limited file-read setup uses `--tools read` in place of
`--no-tools`. Extra extensions, skills and conversation history consume context.
