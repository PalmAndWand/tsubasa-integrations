# Tsubasa with the OpenHands SDK

Use [openhands-sdk.json](../presets/openhands-sdk.json) with the Python
[OpenHands SDK](https://github.com/OpenHands/software-agent-sdk). It uses the
SDK's existing LiteLLM/OpenAI transport and sends your prompts and
`TSUBASA_API_KEY` to `api.tsubasa.sh`. It does not configure the Agent Canvas UI
or OpenHands CLI.

There are two qualified configuration scopes:

- Published `openhands-sdk==1.49.6`: standalone `LLM.generate` text calls.
- Pinned SDK source below: a single native `Agent`/`Conversation` text turn
  using its stock prompt and the built-in `finish` and `think` declarations.

The published agent path is blocked: version 1.49.6 adds `prompt_cache_key`
to Conversation requests, which Tsubasa rejects. Neither `caching_prompt=false`
nor the capability override in this profile prevents that in 1.49.6.
The pinned source checks the override before adding the field. Keep
`capability_overrides.supports_prompt_cache_key=false`; it is required for the
source Conversation path. No transport or request-body patch is needed.

## Standalone LLM calls with the published package

In an isolated Python 3.12+ environment, install the checked SDK and transport
versions:

```sh
python -m pip install 'openhands-sdk==1.49.6' 'litellm==1.103.0' 'openai==2.54.0'
export OH_PERSISTENCE_DIR="$PWD/.openhands-tsubasa"
```

Set `TSUBASA_API_KEY` using your normal secret-management method. Save the
JSON preset in the working directory, then run:

```python
import json
import os
from pathlib import Path

from openhands.sdk import LLM, Message, TextContent

settings = json.loads(Path("openhands-sdk.json").read_text())
llm = LLM(**settings, api_key=os.environ["TSUBASA_API_KEY"])
response = llm.generate(
    messages=[
        Message(role="system", content=[TextContent(text="Reply briefly.")]),
        Message(role="user", content=[TextContent(text="Hello.")]),
    ]
)
for part in response.message.content:
    if isinstance(part, TextContent):
        print(part.text)
```

Change `model` in the preset to `openai/tsubasa-fast` for Fast. The SDK removes
the routing prefix on the wire; Tsubasa receives the canonical alias.
The JSON file contains no credential. `api_mode="chat"` selects Chat Completions.
The output cap is 2,048 tokens. The 30,720-token input setting is SDK metadata;
Tsubasa enforces the combined 32,768-token context limit, including tool schemas
and history. This profile does not establish automatic compaction.

## A bounded native Conversation from pinned source

Install this exact SDK revision in a separate environment instead of the
published SDK:

```sh
python -m pip install \
  'openhands-sdk @ git+https://github.com/OpenHands/software-agent-sdk.git@3311ba9eec5044f40ab5d0b3d7eddc9f7e1e2d14#subdirectory=openhands-sdk' \
  'litellm==1.103.0' 'openai==2.54.0'
export OH_PERSISTENCE_DIR="$PWD/.openhands-tsubasa"
```

Use the same preset and credential setup. In a clean working directory, replace
the `response = llm.generate(...)` and printing block above with:

```python
from openhands.sdk import Agent, Conversation
from openhands.sdk.security.confirmation_policy import AlwaysConfirm

agent = Agent(llm=llm, tools=[])
conversation = Conversation(
    agent=agent,
    workspace=Path.cwd(),
    max_iteration_per_run=1,
)
conversation.set_confirmation_policy(AlwaysConfirm())
try:
    conversation.send_message("Reply briefly with a greeting.")
    conversation.run()
finally:
    conversation.close()
```

`tools=[]` adds no external tools. The SDK still declares its built-in `finish`
and `think` tools. The one-iteration bound and confirmation policy stay enabled.
No tool execution was qualified. Larger project instructions, plugins, history,
or additional tools change the request budget.

## Checked scope

The published package completed eight controlled native LLM requests: both
aliases, JSON/SSE decoding and usage, and invalid-key errors. Each request
passed Tsubasa's actual schema and context checks before the fixture replied.
They used 67 estimated input tokens and reserved 2,048 output tokens.

The pinned source completed a native Conversation text turn on each alias and
surfaced authentication errors for each invalid-key run. All four requests
passed the same checks, at 17,557 estimated input tokens plus 2,048 output,
leaving 13,163 tokens. These are Tsubasa's conservative admission estimates.
The source build used the same dependency versions as the released SDK check.

Verification preserved HOME, used native `OH_PERSISTENCE_DIR`, synthetic keys,
and sandbox restrictions on personal files and external network. An unrelated
OpenAI key did not replace the supplied Tsubasa key. Requests were not filtered.
The full example that adds terminal, editor and task-tracker tools did not reach
HTTP under the local macOS sandbox because its tmux connection was denied;
that setup failure is excluded from transport qualification.

Live inference, tool execution, the Canvas/CLI UI, resumed sessions, compaction,
and unrestricted agent work have not been qualified.
