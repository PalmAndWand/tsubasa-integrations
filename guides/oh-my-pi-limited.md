# Oh-My-Pi text profile

Merge `providers.tsubasa` from [the model configuration](../presets/oh-my-pi-limited.yml)
into `~/.omp/agent/models.yml` (or your existing `PI_CODING_AGENT_DIR/models.yml`).
Keep other providers intact. Set `TSUBASA_API_KEY` to your Tsubasa API key, then run:

```sh
(
  : "${TSUBASA_API_KEY:?Set TSUBASA_API_KEY}"
  omp --model tsubasa/tsubasa-fast --print --no-tools --no-session \
    --no-extensions --no-skills --no-rules --no-title --no-prewalk \
    --no-lsp --no-pty 'Reply with one short greeting.'
)
```

Select `tsubasa/tsubasa-pro` for Pro. The key check is required: Oh-My-Pi treats
an unresolved `apiKey` environment-variable name as a literal key. It does not
fail locally merely because `TSUBASA_API_KEY` is unset.

This profile uses the existing `openai-completions` transport, text input, no
tools, a 32,768-token context declaration and a 2,048-token output limit. It sends
prompts and the Tsubasa key to `https://api.tsubasa.sh/v1`. Keep requests short;
declaring a context window does not guarantee that an arbitrary prompt fits the
server's conservative input accounting.

The official Oh-My-Pi 18.3.5 macOS arm64 release was checked against a controlled
HTTP endpoint with its native loader and CLI. Both aliases decoded streamed text,
reported invalid-key errors and passed the real Tsubasa request schema and
combined input/output check. The stock prompt in this restricted run used at most
7,715 estimated input tokens, plus 2,048 output tokens. The key guard stopped
missing-key calls before HTTP. HOME stayed unchanged; native application paths
and sandbox rules isolated personal configuration and external networking.

This evidence covers short text turns in the shown profile. It does not qualify
the default tool-enabled agent, extensions, interactive UI, long sessions or live
model behavior.

Sources: [18.3.5 release](https://github.com/can1357/oh-my-pi/releases/tag/v18.3.5),
[native configuration](https://github.com/can1357/oh-my-pi/blob/ab2dcbd2abf299139db818330a94777e47d51f68/docs/models.md).
