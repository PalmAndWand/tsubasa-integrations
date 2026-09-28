# Semantic Kernel text service

Save [tsubasa_semantic_kernel.py](../presets/tsubasa_semantic_kernel.py) beside your
application. In an isolated Python environment, install the tested packages:

```sh
python -m pip install semantic-kernel==1.44.1 openai==3.19.2
```

Set `TSUBASA_API_KEY` to your Tsubasa API key. The factory supplies the native
`AsyncOpenAI` client to Semantic Kernel's existing `OpenAIChatCompletion` service:

```python
import asyncio
from semantic_kernel.contents import ChatHistory
from tsubasa_semantic_kernel import create_tsubasa_service, text_settings

async def main():
    service = create_tsubasa_service("tsubasa-fast")
    try:
        history = ChatHistory(system_message="Reply concisely.")
        history.add_user_message("Hello.")
        result = await service.get_chat_message_contents(
            chat_history=history, settings=text_settings())
        print(result[0].content)
    finally:
        await service.client.close()

asyncio.run(main())
```

Use `tsubasa-pro` for Pro. Streaming uses
`service.get_streaming_chat_message_contents(...)` with the same settings.
Requests and the explicit Tsubasa key go to `https://api.tsubasa.sh/v1`; an unrelated
OpenAI key is not selected. Missing `TSUBASA_API_KEY` fails before dispatch.

A fresh `ChatCompletionAgent` can make a bounded first text request with
`instructions=None`, no plugins, and `KernelArguments(settings=text_settings())`.
Both `get_response` and `invoke_stream` were checked. Named instructions are
excluded: Semantic Kernel adds `name` to their system message, which the Tsubasa
schema rejects. Named assistant history and subsequent agent turns are also
outside this recipe's tested scope. Use the service example above for explicit
system instructions without message names.

Controlled checks on Semantic Kernel 1.44.1 covered 16 admitted requests across
the service and fresh agent, both aliases, JSON/SSE decoding and invalid-key
errors. Two named-instruction requests were correctly rejected by the API schema.
Service input was 54 estimated tokens and the fresh agent input was 30, each with
2,048 output tokens reserved. HOME stayed unchanged, with personal files and
external networking isolated.

Output is capped at 2,048 tokens; applications must keep input plus output within
32,768. Tools, structured output, long histories, full agent workflows and live
model behavior are unqualified. Semantic Kernel directs new development to
Microsoft Agent Framework.

Sources: [Semantic Kernel 1.44.1](https://pypi.org/project/semantic-kernel/1.44.1/),
[supplied-client constructor](https://github.com/microsoft/semantic-kernel/blob/ca40aa7226531d28a721d0ca0e451d0aaf86dafc/python/semantic_kernel/connectors/ai/open_ai/services/open_ai_chat_completion.py).
