# GitHub Copilot CLI: restricted file-read profile

Set `TSUBASA_API_KEY`, then from this catalog checkout load the environment
preset and start a bounded native profile:

```sh
. presets/copilot.sh
copilot --available-tools=view --deny-tool shell --deny-tool write --deny-tool url \
  --disable-builtin-mcps --no-custom-instructions --no-auto-update \
  --no-ask-user --no-remote --no-remote-export --no-bash-env \
  -p 'Explain the purpose of this small project.'
```

Set `COPILOT_MODEL=tsubasa-pro` after sourcing the file to use Pro. The native
BYOK route sends prompts and the dedicated key to `api.tsubasa.sh` using OpenAI
Chat Completions. Run it in the shell containing these environment variables.

Use the restricted view profile: the stock 17-tool agent prompt exceeded the
32,768-token total context in our check. Extra tools, instructions and history
also consume that budget. Tool use requires the selected model's server-side
tool capability. The preset's native metadata reserves 1,024 output tokens;
tested requests omitted an explicit output count and used the server's 512-token
default.

Copilot CLI 1.0.88 passed controlled SSE/auth checks and actual file-read round
trips for both aliases with this scope. The largest tested tool-history request
estimated 9,155 input tokens plus 512 output. These checks depend on API support
for `frequency_penalty` and empty assistant `refusal` markers from the tested
Tsubasa API contribution. Deployment and live inference remain unverified; this
is not a qualification of Copilot's full default agent.

See
[GitHub's BYOK guide](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/use-byok-models).
