# Every Code with restricted Tsubasa instructions

This manual profile uses Every Code's existing custom OpenAI Chat Completions
provider. It was checked with the official macOS ARM64 `code 0.6.194` binary.
It does not install a native Tsubasa provider.

**Compatibility requirement:** the Tsubasa API must accept `store: false`.
The source change was validated locally; this check does not establish that it
has been deployed. Every Code always sends this field on its Chat path.

## Install the profile

1. Save [every-code-limited.toml](../presets/every-code-limited.toml) as `config.toml` in a
   separate directory, such as `~/.config/tsubasa-every-code`.
2. Save [every-code-instructions.md](../presets/every-code-instructions.md) alongside it.
   In `config.toml`, replace `/absolute/path/to/every-code-instructions.md` with
   that file's actual absolute path. Do not leave the placeholder unchanged.
3. Set `TSUBASA_API_KEY` in your shell using your usual credential setup. The
   named provider reads this variable and uses `https://api.tsubasa.sh/v1`.
4. Run the restricted profile from your intended working directory:

   ```sh
   CODE_HOME="$HOME/.config/tsubasa-every-code" \
     code exec --profile tsubasa-pro --sandbox read-only --json \
     --max-seconds 60 'Explain a programming concept briefly.'
   ```

Select `--profile tsubasa-fast` for Fast. The profile keeps planning, review,
auto-review, and Auto Drive model selection tied to the chat model; automatic
review and upgrades are disabled. The verified command was normal `exec`, not
Auto Drive. Use `--skip-git-repo-check` only if you intend to run outside a Git
repository.

## Scope and limits

The supplied instructions ask for a brief answer without tool calls. This
replaces Every Code's stock base instructions. `tools.view_image = false`
removes its image-view tool, but other native tool definitions remain in the
request and were included in the budget check.

The stock first request exceeded Tsubasa's estimator at 44,779 input tokens
before any output. The restricted profile estimated 23,541 input tokens and
passed the 32,768-token context limit. These are Tsubasa request-budget
estimates, not a universal tokenizer count. Added workspace instructions or
conversation history can increase them.

The preset sets `model_max_output_tokens = 512`, but version 0.6.194 does not
serialize an output limit on this Chat path. The verified request therefore
relied on Tsubasa's default 512-token output limit. Changing that setting does
not establish a different wire-level output cap.

Both aliases passed native SSE text responses, dedicated-key selection, and
invalid-key errors against a loopback server using the actual API schema and
budget validator. `HOME` was unchanged; personal config discovery and external
network access were blocked. This does not qualify the stock coding prompt,
tool execution, helper agents, TUI interaction, long sessions, or live Tsubasa
inference.
