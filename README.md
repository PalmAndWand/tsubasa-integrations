# Tsubasa integrations

This public catalog contains 34 configuration presets and examples, a Hermes
provider plugin, and setup guides for connecting existing clients to Tsubasa.

> **Validation — September 28, 2026:** Our `/v1/models` check returned HTTP 404.
> These files configure clients; local checks do not establish live chat,
> streaming, tools, structured output, or coding quality.

Most entries are manual settings for a client's existing OpenAI-compatible
transport. Hermes uses its native provider-plugin extension after you install
this separate plugin. None of these files establishes an accepted, built-in
Tsubasa provider in an upstream release.

## Set up a client

Install your chosen client and its normal dependencies first. From a checkout of
this catalog, follow the relevant row below. Merge settings with your existing
configuration rather than replacing it. Set `TSUBASA_API_KEY` through your shell
or secret manager, or use the application's credential field; never save a real
key in these files.

The API base is `https://api.tsubasa.sh/v1`. Public model IDs are `tsubasa-fast`
and `tsubasa-pro`; both have a 32,768-token context window. Maximum output is
8,192 tokens for Fast and 16,384 for Pro. Input and requested output must fit the
context together. Some clients depend on compatible request-field changes
verified locally in the Tsubasa API contribution; those changes are not deployed.

### Command-line clients

The entries below configure locally named providers or profiles. Qwen and Letta
remain blocked for agent use even after configuration.

| Client      | Artifact and installation                                                                                                                                                                     |
| ----------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Pi          | Merge [pi.json](presets/pi.json) into the agent's `models.json`; select `tsubasa/tsubasa-pro` or `tsubasa/tsubasa-fast`.                                                                      |
| gptme       | Add [gptme.toml](presets/gptme.toml) to `config.toml`.                                                                                                                                        |
| OpenCode    | Merge [opencode.json](presets/opencode.json) into `opencode.json`.                                                                                                                            |
| Kilo Code   | Merge [kilo.json](presets/kilo.json) into Kilo's OpenCode-derived provider configuration.                                                                                                     |
| Goose       | Save [goose.json](presets/goose.json) as `tsubasa.json` in the configuration directory's `custom_providers` folder.                                                                           |
| OpenClaw    | Merge [openclaw.json](presets/openclaw.json) into `~/.openclaw/openclaw.json`; select `tsubasa/tsubasa-pro` or `tsubasa/tsubasa-fast`.                                                        |
| OpenHarness | Merge [openharness.json](presets/openharness.json) into `~/.openharness/settings.json`; run `oh setup tsubasa` to store its key.                                                              |
| Plandex     | Merge [plandex.json](presets/plandex.json) with `plandex models custom`, then assign a model-pack role. Self-hosted Plandex only.                                                             |
| OpenGriffin | After setting the key, run `. presets/opengriffin.sh` in the shell that starts the client. [Preset](presets/opengriffin.sh); text chat only.                                                  |
| nanobot     | Merge [nanobot.json](presets/nanobot.json) into `~/.nanobot/config.json`.                                                                                                                     |
| Qwen Code   | [qwen.json](presets/qwen.json) is a blocked configuration reference: merge into `settings.json`, restart, then select Tsubasa in `/model`. Do not treat registration as agent readiness.      |
| Letta Code  | [letta.js](presets/letta.js) is a blocked registration example: save as `~/.letta/mods/tsubasa.js`; `/reload` and `/connect` register it in a local agent. The mod cannot guard all requests. |

### Editors

For Lua presets, merge the returned table into the named plugin's `setup()`
options. The [Neovim chat guide](guides/neovim-chat.md) gives complete loading and
model-selection steps for GP, Parrot, Gen, and ChatGPT.nvim. The
[additional configuration guide](guides/editor-additional.md) covers gptel,
Ellama, Custom LLM Provider, and self-hosted Plandex.

| Client              | Artifact and installation                                                                                                                                                                                          |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Continue            | Merge [continue.yaml](presets/continue.yaml) into `config.yaml`; resolve the key through Continue secrets or its `.env` support.                                                                                   |
| Zed                 | Merge [zed.json](presets/zed.json) into user settings; set the named provider's key through Zed or its environment.                                                                                                |
| CodeCompanion.nvim  | Load [codecompanion.lua](presets/codecompanion.lua) into `require("codecompanion").setup()`.                                                                                                                       |
| avante.nvim         | Load [avante.lua](presets/avante.lua) into `require("avante").setup()`.                                                                                                                                            |
| minuet-ai.nvim      | Load [minuet.lua](presets/minuet.lua) into `require("minuet").setup()`.                                                                                                                                            |
| minuet-ai.el        | Evaluate [minuet.el](presets/minuet.el) in your Emacs configuration.                                                                                                                                               |
| gptel               | Load [gptel.el](presets/gptel.el), then select **Tsubasa** in its menu.                                                                                                                                            |
| Ellama              | Load [ellama.el](presets/ellama.el), then use `ellama-provider-select`; disable tools for the text route.                                                                                                          |
| Custom LLM Provider | Merge [vscode-custom-llm.json](presets/vscode-custom-llm.json) into VS Code settings; store the key with **Custom LLM: Manage providers**.                                                                         |
| gp.nvim             | Load [gp.lua](presets/gp.lua) into `require("gp").setup()`; two named chat/edit agents are configured.                                                                                                             |
| parrot.nvim         | Load [parrot.lua](presets/parrot.lua) into `require("parrot").setup()`; select `:PrtProvider tsubasa`.                                                                                                             |
| gen.nvim            | Load [gen.lua](presets/gen.lua) into `require("gen").setup()`; requires a POSIX shell and curl with `--fail-with-body`.                                                                                            |
| ChatGPT.nvim        | Load [chatgpt.lua](presets/chatgpt.lua) into `require("chatgpt").setup()`; unset conflicting `OPENAI_API_KEY`, `OPENAI_API_HOST`, and `OPENAI_API_TYPE` first. Chat/edit only; legacy completions are unsupported. |

### Applications

The [application setup guide](app-setup.md) covers the UI fields, saved-setting
precedence, and supported scope. Shell presets set initial environment values
for a new process; existing saved application settings can override them.

| Application | Artifact and installation                                                                                                                                                       |
| ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| LibreChat   | Merge [librechat.yaml](presets/librechat.yaml) into `librechat.yaml`; set the key in the server environment.                                                                    |
| AnythingLLM | After setting the key, source [anythingllm.sh](presets/anythingllm.sh) before starting the server, or use **Generic OpenAI** in Settings.                                       |
| Open WebUI  | Source [open-webui.sh](presets/open-webui.sh) for a new deployment, or add an OpenAI API connection in Admin Settings. Merge existing connection lists.                         |
| Dify        | Use [dify.json](presets/dify.json) as a field reference for the official **OpenAI-API-compatible** plugin. It is not an importable app DSL.                                     |
| Langflow    | Source [langflow.sh](presets/langflow.sh) before starting Langflow/LFX, or configure **OpenAI Compatible** under Model Providers. Model discovery uses the configured endpoint. |

### Python examples

Use a separate environment for each framework and install its dependency below.
After setting the key, run `python presets/<filename>` or
reuse the configured client in your application. Each example makes one small
text request and defaults to Pro.

| Framework   | Example                                                  | Dependency used in local verification |
| ----------- | -------------------------------------------------------- | ------------------------------------- |
| LangChain   | [tsubasa_langchain.py](presets/tsubasa_langchain.py)     | `langchain-openai==1.6.6`             |
| Pydantic AI | [tsubasa_pydantic_ai.py](presets/tsubasa_pydantic_ai.py) | `pydantic-ai-slim[openai]==2.51.0`    |
| LlamaIndex  | [tsubasa_llamaindex.py](presets/tsubasa_llamaindex.py)   | `llama-index-llms-openai-like==0.8.0` |
| Haystack    | [tsubasa_haystack.py](presets/tsubasa_haystack.py)       | `haystack-ai==3.2.0`                  |

### Hermes provider plugin

Copy both the [plugin manifest](providers/hermes/plugin.yaml) and
[registration module](providers/hermes/__init__.py) into
`$HERMES_HOME/plugins/model-providers/tsubasa` (default home: `~/.hermes`), keeping
their filenames. Set `TSUBASA_API_KEY` before starting Hermes. The plugin uses
Hermes's provider discovery mechanism; it is not bundled with upstream Hermes.
It does not advertise tools or vision or supply agentic fallback models.

## What has been checked

Verification used synthetic responses and credentials with pinned clients.
These results do not establish live inference or full application readiness.
The private API implementation and verification scripts are not distributed in
this catalog.

- OpenCode 1.18.32, Kilo 7.8.1, Pi 0.87.1, Continue 1.5.47, Goose 1.52.0, and
  OpenClaw 2026.9.6 passed controlled streaming for both models, resumed history,
  HTTP 401 propagation, and request/schema/context checks. Pi additionally
  covered tool-fragment decoding and cancellation. Editor UIs and real models
  were not exercised by these CLI checks.
- **Qwen 0.24.6 and Letta 0.33.2 are blocked:** startup estimates were
  48,637 input + 4,000 output and 99,914 input + 3,886 output, respectively,
  exceeding 32,768 tokens. Qwen safe mode still advertised ten tools; Letta's
  toolset-none mode advertised eighteen. Letta's mod cannot intercept every
  request, and selecting a model when resuming has an upstream bug.
- GP, Parrot, Gen, and ChatGPT.nvim passed 10 real local requests across both
  models through schema and budget checks. Gen rendered the fixture stream and
  preserved shell-sensitive prompt text. ChatGPT.nvim's interactive window was
  not checked. See the [pinned revisions and scope](guides/neovim-chat.md#recorded-local-checks).
- AnythingLLM, Dify, and Langflow passed controlled text/streaming and credential
  checks for both models. Open WebUI also passed real backend startup, SQLite,
  admin sign-in, model listing, middleware, text/SSE and invalid-session/key
  handling. Browser/socket chat, tools/RAG, and live inference remain unverified.
  See the [application evidence](app-setup.md#controlled-verification).
- Hermes and OpenHarness passed native HTTP streaming for both aliases,
  credential isolation, and request schema/context checks. OpenHarness also
  decoded fragmented tool calls and forwarded tool-result history. nanobot
  passed configuration and credential checks. OpenGriffin passed text transport;
  its connector lacks streaming and tool-result support.
- The four Python examples decoded one controlled text response per framework;
  streaming and live behavior were not tested. CodeCompanion passed
  adapter/request checks.
- gptel, Ellama, Minuet Emacs, Minuet Neovim, Avante, and Custom LLM Provider
  passed 22 actual local HTTP requests covering both aliases, streaming, and
  HTTP 401. Full graphical editor sessions were not checked. Plandex passed
  its CLI loader and model conversion; server sessions remain unverified.
  Zed and LibreChat were reviewed from source or configuration documentation.
- The installable gptme plugin source is proposed in
  [PR #1](https://github.com/PalmAndWand/tsubasa-integrations/pull/1). Its installed
  entry point and real gptme HTTP transport passed eight controlled requests,
  including text, streaming, history, and HTTP 401. No package release is claimed.

Keep unqualified tools, vision, embeddings, and structured output disabled.
Begin with plain text and a small output limit, then qualify the specific
client workflow before relying on agent use.
