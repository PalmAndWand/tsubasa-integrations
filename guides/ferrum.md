# Ferrum

Use [ferrum.toml](../presets/ferrum.toml) with Ferrum 0.7.9 on Linux.
Merge its provider and model entries with your configuration in
`~/.config/ferrum/config.toml`, or put the complete file at
`$FERRUM_CONFIG_DIR/config.toml` in a separate directory. The complete example
selects Fast, turns thinking off, and sets the operating context to 32,768.

Set `TSUBASA_API_KEY` through your usual secret-management method, then run:

```sh
: "${TSUBASA_API_KEY:?Set TSUBASA_API_KEY}"
ferrum --provider tsubasa --model tsubasa-fast --thinking off \
  --no-tools --no-mcp --safety high -p "Reply briefly with a greeting."
```

Use `--model tsubasa-pro` for Pro. The existing OpenAI-compatible transport sends
your prompt and dedicated key to `https://api.tsubasa.sh/v1`. No provider adapter
or response rewriting is required. Both public aliases have a 32,768-token
context window. Ferrum omits an explicit output cap in this route, so Tsubasa
uses its 512-token default. Ferrum's own character-based context estimate does
not replace Tsubasa's conservative admission check.

This profile disables tools and MCP and qualifies short text turns only.
`max_tool_rounds=1` is a secondary loop bound; it is not a request-token cap.
Merge settings carefully when you already have other providers configured.

## Checked scope

The official checksum-verified Linux x86-64 binary completed six controlled
native CLI requests: JSON and SSE for both aliases, and invalid-key errors
for both aliases. All six passed the real API schema and context checks before
the fixture replied, with at most 3,236 estimated input tokens plus 512 output.
The invalid-key commands exited with failure and did not fall back to an
unrelated OpenAI key.

The test used an isolated Docker container with no external network, no personal
files mounted, a read-only filesystem, native configuration/data directories,
and synthetic credentials. No HOME value was changed. The binary's published
build provenance points to source revision
`f31151d34fade3ef88104a33ba2a4042e689be35`.

Interactive sessions, live model discovery, model tool execution, compaction,
long contexts and live inference remain unqualified. Ferrum's canonical project
is [on Codeberg](https://codeberg.org/ominiverdi/ferrum); its GitHub repository
is a passive mirror.
