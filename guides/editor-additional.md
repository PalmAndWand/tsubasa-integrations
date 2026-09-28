# Additional editor configurations

These presets use each application's existing custom-provider support. They
add named configurations without modifying the application.

Set `TSUBASA_API_KEY` in the environment inherited by Emacs. Load `gptel.el` from
your Emacs configuration and choose **Tsubasa** in the gptel menu. Load `ellama.el`
to add **Tsubasa Fast** and **Tsubasa Pro** to `ellama-providers`, then choose one
with `ellama-provider-select`. Set `ellama-tools-enabled` to `nil` for this text
route. Neither preset changes your default provider.

For VS Code, install **Custom LLM Provider** by Martin Riha. Merge the entries in
`vscode-custom-llm.json` into User Settings JSON, keeping existing entries. Run
**Custom LLM: Manage providers**, select **Tsubasa**, then **Edit API key**.
The extension stores the key in SecretStorage. Select the model under **Custom
LLM** in Copilot Chat; it may first need enabling in **Chat: Manage Language
Models**. Image input and tool calling remain disabled.

For self-hosted Plandex, set `TSUBASA_API_KEY`, run `plandex models custom`, and
merge `plandex.json` into the custom models file. Assign `tsubasa/fast` or
`tsubasa/pro` to a custom model-pack role. Plandex Cloud does not allow arbitrary
custom providers. The example uses XML output and an 8,192-token output cap for
both models, leaving room in the 32,768-token shared context.

## Recorded local checks

Controlled HTTP checks used synthetic credentials and responses. Actual gptel,
Ellama, Minuet Emacs, Minuet Neovim, Avante, and Custom LLM Provider transports
passed 22 requests across both model aliases, including streaming and
HTTP 401 propagation. Request bodies passed the Tsubasa schema and context
budget checks. Custom LLM Provider used a substituted VS Code UI surface while
keeping its real HTTP helper. These checks do not cover full graphical editor
sessions or live inference.

The Plandex example passed its actual CLI loader, schema, and provider/model
conversion. Server planning sessions and inference were not exercised.
