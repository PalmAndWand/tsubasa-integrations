# Tsubasa in RA.Aid

Use RA.Aid's existing `openai-compatible` provider for both the main and expert
model routes. The tested source is
[`e71bb83`](https://github.com/ai-christianson/RA.Aid/tree/e71bb83dcfdf8796d41c746ad99bf4838d1d5914), version 0.30.2.

Install that checkout with its committed lockfile:

```sh
uv sync --frozen --no-dev
```

The lockfile selects LangChain 0.3.25, LangChain OpenAI 0.3.18, LangGraph 0.4.5,
and OpenAI 1.82.1. An unconstrained fresh installation selected newer packages
and failed before startup because RA.Aid imports a removed LangGraph module.
The checked recipe therefore requires the committed lockfile.

Set `TSUBASA_API_KEY` through your normal secret-management method. From a small
working directory, run the installed CLI with explicit main and expert
credentials and endpoints:

```sh
OPENAI_API_KEY="${TSUBASA_API_KEY:?Set TSUBASA_API_KEY}" \
EXPERT_OPENAI_API_KEY="$TSUBASA_API_KEY" \
OPENAI_API_BASE=https://api.tsubasa.sh/v1 \
EXPERT_OPENAI_API_BASE=https://api.tsubasa.sh/v1 \
LLM_MAX_RETRIES=0 LLM_REQUEST_TIMEOUT=15 \
/path/to/RA.Aid/.venv/bin/ra-aid \
  --provider openai-compatible --model tsubasa-fast \
  --expert-provider openai-compatible --expert-model tsubasa-fast \
  --research-only --recursion-limit 1 \
  -m 'Explain this small repository without making changes.'
```

Replace the executable path with your checkout's actual path. Select Pro by
changing both model arguments to `tsubasa-pro`. These environment assignments
apply only to this command. The key guard prevents an absent Tsubasa credential
from silently using an ambient OpenAI key. Prompts and credentials are sent to
`api.tsubasa.sh`.

This provider path does not serialize an output cap, so the checked requests
use Tsubasa's default 512-token output allowance. RA.Aid's `--num-ctx` and
`--expert-num-ctx` flags are documented for Ollama and do not establish a limit
on this transport. `--recursion-limit` limits nested agent recursion; it is not
a hard limit on model requests. Keep tasks and repository context small within
Tsubasa's combined 32,768-token window.

Controlled checks exercised the native main and expert client factories for
both aliases: JSON, streaming, dedicated credential selection, HTTP 401, and
missing-key failure before dispatch. The actual CLI also loaded its stock
research prompt and textual tool descriptions, parsed a synthetic completion
function call, ran its native research-completion function, and exited
successfully on both aliases. All 14 captured requests passed the actual
Tsubasa schema and context check before the loopback fixture replied. Each
initial CLI request estimated 23,659 input tokens plus 512 output.

The fixture used synthetic credentials, a temporary working directory, an
unchanged HOME, and a sandbox blocking personal files and external network.
It did not qualify arbitrary tool execution, implementation/planning stages,
Aider delegation, cost estimates, long sessions, or live inference. The
research-only option still exposes tools; this is not a security sandbox or a
read-only execution guarantee.
