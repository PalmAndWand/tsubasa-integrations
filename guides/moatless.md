# Moatless Tools

Use Moatless Tools' existing LiteLLM/OpenAI completion classes. These are custom
model configurations, not entries in Moatless's verified-model benchmark table.
The checked source is
[`011ead5`](https://github.com/aorwall/moatless-tools/tree/011ead57a5c81664e9c45e07e1f50b17e695cc63)
(project version 0.1.1), with LiteLLM 1.76.0 and OpenAI Python 1.101.0. This is
`moatless-tools`; the paper's `moatless-tree-search` project is separate.

Follow upstream's source installation instructions at that revision. Download
[moatless.json](../presets/moatless.json), set `TSUBASA_API_KEY`, and load either entry with
the native factory:

```python
import asyncio
import json
import os
from pathlib import Path

from moatless.actions import Respond
from moatless.agent import ActionAgent
from moatless.completion.base import BaseCompletionModel

settings = json.loads(Path("moatless.json").read_text())["tsubasa-fast"]
settings["model_api_key"] = os.environ["TSUBASA_API_KEY"]
model = BaseCompletionModel.from_dict(settings)
agent = ActionAgent(
    completion_model=model,
    system_prompt="You are a helpful assistant that can answer questions.",
    actions=[Respond()],
)
observation = asyncio.run(agent.run_simple("Explain a programming concept."))
print(observation.message)
```

Select `tsubasa-pro` from the JSON for Pro. The `openai/` prefix selects
LiteLLM's existing transport; the API receives the public alias without that
prefix. The key assignment is explicit Python code, not automatic JSON
environment-variable expansion.

Both entries cap output at 4,096 tokens within the shared 32,768-token context
limit. Prompts, action schemas and history must fit the remaining space. This
does not configure a benchmark runner's memory or truncation policy. Moatless
does not have verified pricing for these custom aliases; a zero local cost
estimate does not mean inference is free.

A controlled local HTTP fixture verified both aliases, Bearer authentication,
401 errors, JSON response parsing, ReAct `Finish` parsing/execution, and the native
`ActionAgent.run_simple` → `Respond` flow above. All unchanged serialized
requests passed Tsubasa's real schema and context-budget checks. The checks used
the pinned source and its completion/action dependency subset, not a full
Docker or benchmark deployment. They establish local protocol behavior, not
live tool-calling or reasoning quality. Streaming, SWE-bench, repository editing
and embedding/index services remain unqualified.
