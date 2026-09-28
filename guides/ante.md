# Ante

Merge [ante.json](../presets/ante.json) into `~/.ante/catalog.json`, preserving
other provider entries. Set `TSUBASA_API_KEY` in your shell or secret manager.
The native `ANTE_HOME` setting can select a separate Ante configuration folder.

```sh
ante --provider tsubasa --model tsubasa-fast --short-prompt \
  --no-skills --disable-auto-memory --permission-mode strict
```

Select `tsubasa-pro` for the other alias. The profiles use Ante's existing Chat
Completions transport, declare image input unsupported, omit reasoning-effort
fields, and reserve 512 output tokens inside a 32,768-token total context.
Prompts and the dedicated key go to `api.tsubasa.sh`.

Start with a small project. Added instructions, tools, files and history can
exceed the context limit. Agent tools also require the selected model's current
tool capability; the catalog entry does not enable server-side capabilities.

Ante 0.2.5 passed controlled native CLI text/streaming/auth checks and actual
Read-tool round trips for both aliases. The largest tested tool-history request
estimated 24,105 input tokens plus 512 output. These loopback checks used
synthetic credentials and preserved HOME; live inference and long sessions
remain unqualified.

See the
[native catalog reference](https://docs.antigma.ai/reference/catalog-reference).
