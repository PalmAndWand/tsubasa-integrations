# MetaGPT

Use MetaGPT's existing `openai` provider with a custom URL and public alias.
This is a manual configuration, not a new built-in provider. The checked source
is [`11cdf46`](https://github.com/FoundationAgents/MetaGPT/tree/11cdf466d042aece04fc6cfd13b28e1a70341b1f),
using Python 3.11.13, OpenAI Python 1.64.0 and Pydantic 2.7.4.

Follow MetaGPT's source setup for that revision. Copy
[metagpt.yaml](../presets/metagpt.yaml) into your MetaGPT project's `config/config2.yaml`,
merging the `llm` section if the file already exists. Replace the key placeholder
with your Tsubasa key. YAML does not automatically expand `$TSUBASA_API_KEY`.
Use `model: tsubasa-pro` for Pro. MetaGPT also reads
`~/.metagpt/config2.yaml`, whose values override the project file; inspect your
effective settings before a request. `METAGPT_PROJECT_ROOT` can select a
separate project directory without changing `HOME`.

The preset sets `max_token: 4096`. MetaGPT's `context_length` means maximum
input tokens, so it is set to 28,672 to leave room within Tsubasa's 32,768-token
total limit. MetaGPT defaults to no compression; this value alone does not
enforce truncation. Keep input and output within the API's actual budget.

The native factory can load the selected configuration directly:

```python
import asyncio

from metagpt.config2 import Config
from metagpt.provider.llm_provider_registry import create_llm_instance

async def main():
    llm = create_llm_instance(Config.default().llm)
    try:
        print(await llm.aask("Explain a programming concept.", stream=False))
    finally:
        await llm.aclient.close()

asyncio.run(main())
```

A controlled local HTTP fixture verified the native config loader and provider
factory for both aliases, JSON and SSE text, Bearer authentication, 401 errors,
`aask`'s built-in system prompt, and `aask_code`'s built-in function schema and
returned argument parsing. The returned code was not executed. Every unchanged
request passed Tsubasa's real schema and budget checks with the 4,096-token
output cap. Tests used the pinned source and its provider/tool import
dependencies. Full team workflows, repository editing, embeddings and live
inference remain unqualified.

At this revision the streaming parser ignores a usage-only SSE frame with
`choices: []`. Local token accounting then falls back to an estimator that does
not recognize these aliases. Non-streaming responses preserve returned token
counts, but MetaGPT's price table does not contain these models. Do not treat
its zero cost display as an accurate bill or budget guard.
