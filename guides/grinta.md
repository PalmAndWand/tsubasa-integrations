# Grinta

Merge [grinta.json](../presets/grinta.json) into Grinta's `settings.json`. Set
`LLM_API_KEY` through your shell or Grinta's local `.env` file. Installed Grinta
uses `~/.grinta/settings.json`; `APP_ROOT` can select a separate configuration
directory. See
[Grinta's settings guide](https://github.com/josephsenior/Grinta-Coding-Agent/blob/main/docs/SETTINGS.md)
for configuration precedence.

The recipe uses Grinta's existing `openai` inference adapter, with
`https://api.tsubasa.sh/v1` as its base URL. Select `tsubasa-pro` instead of
`tsubasa-fast` to use the other alias. The configuration sends prompts and the
configured key to `api.tsubasa.sh`.

Keep the 32,768-token context and 4,096-token output request in the example.
Prompts, tools and history must fit alongside the output reservation. Grinta's
agent requires tool calls to be enabled for the endpoint and model; selecting a
custom alias does not enable this capability.

The native settings loader and inference adapter passed controlled HTTP checks.
The complete agent CLI has not been qualified with this recipe.
