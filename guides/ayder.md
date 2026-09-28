# Ayder

Use Tsubasa through Ayder's existing OpenAI driver. Save this configuration as
`tsubasa.toml` outside your project repository:

```toml
config_version = "2.0"

[app]
provider = "tsubasa"

[llm.tsubasa]
driver = "openai"
base_url = "https://api.tsubasa.sh/v1"
api_key = "YOUR_TSUBASA_API_KEY"
model = "tsubasa-fast"
num_ctx = 32768
max_output_tokens = 8192
think = false
```

Replace `YOUR_TSUBASA_API_KEY` with your key. Ayder reads `api_key` literally;
writing `$TSUBASA_API_KEY` there does not expand the environment variable. On
macOS or Linux, restrict the local file with `chmod 600 tsubasa.toml`.

Run `ayder --config /absolute/path/to/tsubasa.toml`. To use Pro, change `model`
to `tsubasa-pro`. Both aliases have a 32,768-token context window. The
8,192-token output setting leaves room for input; Fast supports up to 8,192
output tokens and Pro up to 16,384, within the total context window.

Controlled checks at [Ayder revision a2586d1](https://github.com/ayder/ayder-cli/tree/a2586d1124874142eabc2095d1b3bd78c0d1b062) loaded this TOML through the native loader and shared `create_runtime`, including its stock prompt and tool declarations. Both aliases decoded JSON and streamed text. Invalid and empty literal credentials failed without falling back to an ambient OpenAI key. All six captured requests passed the Tsubasa schema and context checks. These checks cover the shared runtime first response; the full agent loop, UI, and live inference remain unqualified.
