# Swival

Use Tsubasa through Swival's generic OpenAI-compatible provider. Add a profile
to `~/.config/swival/config.toml` (or `$XDG_CONFIG_HOME/swival/config.toml`):

```toml
[profiles.tsubasa]
provider = "generic"
base_url = "https://api.tsubasa.sh/v1"
model = "tsubasa-fast"
max_context_tokens = 32768
max_output_tokens = 8192
```

Set `TSUBASA_API_KEY`, then run:

```sh
OPENAI_API_KEY="${TSUBASA_API_KEY:?Set TSUBASA_API_KEY}" \
    swival --profile tsubasa "task"
```

The generic provider reads `OPENAI_API_KEY`; this assignment affects only the
Swival command. The guard stops if your Tsubasa key is absent.

Select Pro by adding `--model tsubasa-pro`. Both aliases have a 32,768-token
context window. The 8,192-token output reservation leaves room for the prompt
and tool declarations. Fast supports up to 8,192 output tokens; Pro supports up
to 16,384, within the same total context limit.

Controlled checks at [Swival revision 7535c4c](https://github.com/Swival/swival/tree/7535c4c2c7d40d3c12af358ba47c2c3ef1b89d6e) exercised this native CLI profile against a loopback endpoint. Both aliases decoded JSON and streamed text, an invalid key produced HTTP 401, and a missing key stopped before dispatch. All five captured requests passed the Tsubasa schema and context checks. The measured initial request reserved 17,429 input and 8,192 output tokens. Full tool execution, long conversations, and live inference remain unqualified.
