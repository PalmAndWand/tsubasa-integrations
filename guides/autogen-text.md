# AutoGen text client

Save [tsubasa_autogen.py](../presets/tsubasa_autogen.py) beside your application.
In an isolated Python environment, install the tested packages:

```sh
python -m pip install 'autogen-ext[openai]==0.7.5' autogen-agentchat==0.7.5 openai==3.19.2
```

Set `TSUBASA_API_KEY` to your Tsubasa API key. For a short text turn:

```python
import asyncio
from autogen_core.models import SystemMessage, UserMessage
from tsubasa_autogen import create_tsubasa_client

async def main():
    client = create_tsubasa_client("tsubasa-fast")
    try:
        result = await client.create([
            SystemMessage(content="Reply concisely."),
            UserMessage(content="Hello.", source="user"),
        ])
        print(result.content)
    finally:
        await client.close()

asyncio.run(main())
```

Use `tsubasa-pro` to select Pro, or `client.create_stream(...)` for streaming.
The native client sends requests to `https://api.tsubasa.sh/v1` with the Tsubasa
key. It requires that key explicitly, even if an unrelated OpenAI key exists.
`include_name_in_message=False` is required for this route. The conservative
`model_info` disables tools, vision and structured output; it does not claim those
capabilities from the alias name.

`AssistantAgent("tsubasa_text", model_client=client)` also supports a bounded
first text turn. Omit `tools` entirely: AutoGen 0.7.5 rejects even `tools=[]` when
`function_calling=False`. `model_client_stream=True` selects its streaming path.
No handoffs, plugins or tools were exercised.

Both aliases passed controlled JSON/SSE response decoding and invalid-key handling
through the client and native `AssistantAgent`: 16 actual requests passed the
Tsubasa schema and combined context check. Missing-key factory calls stopped
before HTTP. The tested first-agent input was 178 estimated tokens, with a
2,048-token output reserve. HOME was preserved and external networking and
personal files were isolated.

The factory caps output at 2,048 tokens. It does not install automatic context
management for these custom model aliases: keep total input plus reserved output
within 32,768. Long histories, multi-agent operation, tools and live model behavior
are unqualified. AutoGen is in maintenance mode; new development is directed to
Microsoft Agent Framework.

Sources: [AutoGen 0.7.5](https://pypi.org/project/autogen-ext/0.7.5/),
[native compatible client](https://github.com/microsoft/autogen/blob/027ecf0a379bcc1d09956d46d12d44a3ad9cee14/python/packages/autogen-ext/src/autogen_ext/models/openai/_openai_client.py).
