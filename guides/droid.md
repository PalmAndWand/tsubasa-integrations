# Factory Droid

Set `TSUBASA_API_KEY` in your shell or secret manager. From this catalog
checkout:

```sh
droid exec --settings "$PWD/presets/droid.json" --model custom:Tsubasa-0 \
  --disable-builtin-skills 'Explain the purpose of this small project.'
```

The native settings file expands the key from the environment. Its custom
provider uses `generic-chat-completion-api`; Droid's `openai` type selects a
different protocol. The configuration sends prompts and the key to
`api.tsubasa.sh`. Image input is disabled.

To select Pro, change the example's `model` value to `tsubasa-pro`. Preserve the
512-token output setting. Both aliases allow 32,768 tokens for input, tools and
output together. Merge the custom model into your existing settings if you want
to retain other models; its generated selection ID may then have a different
index, so select it through Droid's model picker.

Droid 0.228.0 passed controlled JSON CLI output, streamed completions and auth
checks and native Read-tool round trips for both aliases. The tested prompt and
tool-result history already used 30,676 input tokens, leaving little room with
512 tokens reserved for output. Larger projects and long sessions are not
qualified. Tools require the endpoint and model to support them; this recipe
does not enable that server capability. Live inference was not exercised.

See [Factory's BYOK guide](https://docs.factory.ai/model-independence/byok).
