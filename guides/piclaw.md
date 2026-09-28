# PiClaw

Merge [piclaw.json](../presets/piclaw.json) into PiClaw's Pi agent `models.json`.
Use the agent directory selected by `PICLAW_PI_AGENT_DIR` (or
`PI_CODING_AGENT_DIR`); without an override it is `~/.pi/agent`. Preserve your
existing providers when merging.

Set `TSUBASA_API_KEY` in the environment of the PiClaw process and reload its
model configuration or restart the application. Select `tsubasa/tsubasa-fast`
or `tsubasa/tsubasa-pro` in the model picker. The entry uses PiClaw's native
model/credential runtime and Pi's Chat Completions transport, sending prompts
and `TSUBASA_API_KEY` to `api.tsubasa.sh`.

Use the complete model definitions in this file. The generic provider wizard
does not expose every output/compatibility setting from `models.json` and can
replace a provider block when saved. Both aliases have a 32,768-token context;
maximum output is 8,192 for Fast and 16,384 for Pro. Prompts, tools, workspace
resources and requested output must fit together. Agent tools require support
from the selected endpoint and model; registering a model does not enable it.

The production model/credential runtime passed eight controlled HTTP requests
covering text, tool history and rejected keys, plus a pre-dispatch abort check
that sent no HTTP request. These checks preserved HOME.
The full agent, UI and live inference remain unqualified.
