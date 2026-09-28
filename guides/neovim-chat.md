# Tsubasa chat presets for Neovim

These presets configure the existing Chat Completions transports in gp.nvim,
parrot.nvim, gen.nvim, and ChatGPT.nvim. They use the public `tsubasa-pro` and
`tsubasa-fast` aliases and read credentials from `TSUBASA_API_KEY`.

These Tsubasa-owned files register entries in your local plugin configuration. A
[Parrot preview example](https://github.com/frankroeder/parrot.nvim/pull/201) is
submitted as a draft. None is accepted as a stock upstream provider.

> **Validation:** The September 28, 2026 check of `/v1/models` returned HTTP 404.
> Local fixture checks do not qualify live inference,
> tools, structured output, or model quality. gp.nvim also requires the shared
> API support for `max_completion_tokens` and `top_p` that has been implemented
> locally but is not deployed.

## Set up a preset

Install the selected plugin and its documented dependencies through your
existing Neovim plugin manager. Set `TSUBASA_API_KEY` in the environment that
starts Neovim; never paste a key into a preset or tracked configuration.

Copy the selected Lua file into your Neovim configuration's `tsubasa` directory.
Merge its returned table with your existing plugin options before calling
`setup()`. The examples below show a fresh configuration.

### gp.nvim

Use [gp.lua](../presets/gp.lua) to register two named agents for chat and
editing. The default chat and command agent is **Tsubasa Pro**.

```lua
require("gp").setup(dofile(vim.fn.stdpath("config") .. "/tsubasa/gp.lua"))
```

Open a chat with `:GpChatNew` and switch between the Tsubasa agents with
`:GpSelectAgent`. The plugin's standard request includes `top_p: 1` and an
output limit of 4096 tokens. The preset does not remove or rewrite those fields.
Image and speech commands are outside this configuration's supported scope.

### parrot.nvim

Use [parrot.lua](../presets/parrot.lua) to add the named `tsubasa` provider. The
preset keeps model discovery local and uses Tsubasa Fast for chat titles.

```lua
require("parrot").setup(dofile(vim.fn.stdpath("config") .. "/tsubasa/parrot.lua"))
```

Select `:PrtProvider tsubasa`, then start `:PrtChatNew`. Use
`:PrtModel tsubasa-pro` or `:PrtModel tsubasa-fast` inside a chat buffer to
change its model. The same command outside a chat buffer changes the editing
model. Chat and editing requests have a 4096-token output limit; titles use 64
tokens.

### gen.nvim

Use [gen.lua](../presets/gen.lua) to replace the Ollama command with
authenticated Chat Completions. The preset keeps the two model choices local and
disables Ollama startup.

```lua
require("gen").setup(dofile(vim.fn.stdpath("config") .. "/tsubasa/gen.lua"))
```

Run `:Gen` and choose a prompt. Use `:lua require("gen").select_model()` to
switch models. The configured command requires a POSIX shell and curl with
`--fail-with-body` support. It expands the API key at execution time and streams
the response through the plugin's existing parser.

The initialization hook selects inline JSON because this pinned plugin version's
temporary-file branch doubles literal percent signs in prompts. It does not
modify the prompt or response, start another service, or add a protocol filter.
Keep the output limit and `stream = true` when customizing this preset; the
plugin's Chat Completions parser expects streamed deltas.

### ChatGPT.nvim

Use [chatgpt.lua](../presets/chatgpt.lua) for the chat and edit commands. This
plugin gives `OPENAI_API_KEY`, `OPENAI_API_HOST`, and `OPENAI_API_TYPE`
precedence over configuration commands. The preset rejects those variables to
prevent an unintended host or credential selection.

Start a separate Neovim process without those overrides:

```sh
env -u OPENAI_API_KEY -u OPENAI_API_HOST -u OPENAI_API_TYPE nvim
```

Load the preset after installing the plugin's dependencies:

```lua
require("chatgpt").setup(dofile(vim.fn.stdpath("config") .. "/tsubasa/chatgpt.lua"))
```

Use `:ChatGPT` or `:ChatGPTEditWithInstructions`. To choose Tsubasa Fast, change
both `openai_params.model` and `openai_edit_params.model` to `tsubasa-fast`
before calling `setup()`. The chat configuration caps output at 4096 tokens,
including edit requests that inherit those parameters.

`ChatGPTCompleteCode` and actions using legacy `/completions` are unsupported.
Do not redirect those requests to `/chat/completions`; their request format is
different. Other custom action formats need separate verification.

## Recorded local checks

The recorded checks used real plugin loaders and HTTP requests to a loopback
fixture with synthetic credentials. All 10 captured requests passed Tsubasa's
request schema and model budget helper. No request went to a live provider.
The checks and private API implementation are not included in this catalog.

The checks used these upstream revisions:

| Folder         | Pinned upstream revision                                                                                                       |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| `gp-nvim`      | [Robitx/gp.nvim at c37f154](https://github.com/Robitx/gp.nvim/tree/c37f154b97690c4925fef4e35ffdbf2c844b5f4e)                   |
| `parrot-nvim`  | [frankroeder/parrot.nvim at 86caf5a](https://github.com/frankroeder/parrot.nvim/tree/86caf5ac682049e4025ba5272468161f459a8048) |
| `gen-nvim`     | [David-Kunz/gen.nvim at c8e1f57](https://github.com/David-Kunz/gen.nvim/tree/c8e1f574d4a3a839dde73a87bdc319a62ee1e559)         |
| `chatgpt-nvim` | [jackMort/ChatGPT.nvim at 5c54a7e](https://github.com/jackMort/ChatGPT.nvim/tree/5c54a7e9de67e2f8f8c3ed60f872f4a34a3e65ff)     |

GP, Parrot, and Gen sent streaming requests for both public models. ChatGPT.nvim
sent streaming chat and nonstreaming edit requests for both models. Gen rendered
the stream and preserved shell-sensitive prompt text exactly. ChatGPT.nvim
validation loaded its real configuration and API modules; its interactive chat
window was not exercised. These results do not qualify live model behavior.
