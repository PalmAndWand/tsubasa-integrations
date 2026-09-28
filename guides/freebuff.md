# Freebuff

Use Tsubasa through Freebuff's existing OpenAI-compatible BYOK connection.
Install the [Freebuff CLI](https://freebuff.com/cli) and use a build whose
`/byok` command lists `add`, `validate`, and `select`.

Export your Tsubasa key in the terminal that launches Freebuff:

```sh
export TSUBASA_API_KEY="your-tsubasa-api-key"
freebuff
```

Inside Freebuff, create and select a connection for Tsubasa Fast:

```text
/byok add tsubasa openai-compatible tsubasa-fast TSUBASA_API_KEY https://api.tsubasa.sh/v1 --context-window=32768 --max-output-tokens=512
/byok validate tsubasa
/byok select tsubasa
```

To add Tsubasa Pro as a separate connection:

```text
/byok add tsubasa-pro openai-compatible tsubasa-pro TSUBASA_API_KEY https://api.tsubasa.sh/v1 --context-window=32768 --max-output-tokens=512
/byok validate tsubasa-pro
/byok select tsubasa-pro
```

These commands create local named connections with a 32,768-token context and a
512-token output limit per completion. Keep both limit flags: Freebuff can
automatically expand the context when it interprets a connection's limits as
unconfigured defaults.

Pass the environment variable name `TSUBASA_API_KEY` to `/byok add`; do not
paste the key into the command. Freebuff stores the reference and reads the key
from the environment when resolving the connection.

Freebuff checks the provider's `/v1/models` endpoint before selecting a
connection. If validation fails, correct the reported URL or connection problem
and retry `/byok validate`. Selecting a different connection starts a new
transcript. Use `/byok list` to inspect saved connections and `/byok off` to
return to Freebuff's default inference.

## Checked scope

The native connection store, limit resolver and model factory at source revision
`6fc07b5190420d51004d5bcca29b24d16df9c490` passed five controlled HTTP requests,
including text, streaming and rejected credentials. Missing/revoked credentials
sent no request. The published SDK 0.10.7 does not contain this BYOK interface;
these checks used the pinned source. Complete CLI/agent sessions and live
inference remain unqualified, and connection selection depends on successful
model discovery.
