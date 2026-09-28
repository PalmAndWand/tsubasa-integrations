# Tsubasa in Grok Build

Use [grok-build.toml](../presets/grok-build.toml) with the official
[xAI Grok Build](https://github.com/xai-org/grok-build) client. This adds custom
named models through its existing Chat Completions backend; Tsubasa is not a
stock provider in Grok Build. The community project named Grok CLI is a different
client and is not covered here.

Install Grok Build from its official instructions. The profile was checked with
the macOS ARM64 release `1.0.41 (4220f3b224a6)`. From the directory containing the
downloaded preset, create a dedicated Grok configuration:

```sh
export GROK_HOME="$PWD/.grok-tsubasa"
mkdir -p "$GROK_HOME"
cp grok-build.toml "$GROK_HOME/config.toml"
```

Set `TSUBASA_API_KEY` in your environment using your normal secret-management
method, then list the models and run a short turn in a directory you intend the
client to access:

```sh
grok models
grok --model tsubasa-pro --single 'Reply briefly with a greeting.' \
  --output-format json --tools read_file --no-subagents \
  --disallowed-tools search_tool,use_tool --disable-web-search --max-turns 1 \
  --leader-socket "$GROK_HOME/leader.sock"
```

Use `--model tsubasa-fast` for Fast. Keep the command's tool restrictions for
this tested profile. Only `read_file` is exposed to the main turn; a file read
was not exercised by the validation fixture.

The preset declares a 32,768-token context and a 4,096-token response budget.
Keep `models.session_summary = "tsubasa-fast"`: the client's separate session
title request otherwise selects a Grok model. The title request uses its own
100-token response budget. Remote configuration fetches, managed MCP servers,
telemetry, turn summaries, and title refreshes are disabled in this profile.

Verification used an isolated configuration and a loopback HTTP fixture with
synthetic keys. Native model listing, both public aliases, streamed responses,
usage, and invalid-key errors passed. All eight requests, including the native
title helper, passed Tsubasa's real request schema and context-budget check.
The largest main request was estimated at 12,453 input tokens plus 4,096 output
tokens. These are Tsubasa admission estimates, not a universal tokenizer count.

Live inference, the interactive UI, file-tool execution, and long-session
compaction have not been verified. No upstream acceptance is implied. The
checked public source was `f0e3be1100ef5252488e3be8bb0e91cf68d8c305`; the released
binary reports a different internal build commit that is not available in that
public source export.
