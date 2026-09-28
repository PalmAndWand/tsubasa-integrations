# Tsubasa in SWE-agent

Use the existing LiteLLM OpenAI-compatible route with the upstream
thought/action configuration. This setup was checked against SWE-agent
[revision 3ea751c](https://github.com/SWE-agent/SWE-agent/tree/3ea751c087f32b16e039a2233dd6eefecef325d5), version 1.1.0, with LiteLLM 1.103.0.
Install SWE-agent normally from that source checkout and keep its supported
SWE-ReX environment configuration.

Save [swe-agent.yaml](../presets/swe-agent.yaml) and
[tsubasa-sweagent-costs.json](../presets/tsubasa-sweagent-costs.json) in the
checkout's working directory. Set `TSUBASA_API_KEY` through your normal secret
management, then merge the two native configurations in this order:

```sh
: "${TSUBASA_API_KEY:?Set TSUBASA_API_KEY}"
sweagent run \
  --config config/sweagent_0_7/07_thought_action.yaml \
  --config swe-agent.yaml \
  --problem_statement.text 'Your small repository task'
```

Use your existing environment/repository options for the task. To select Pro,
add `--agent.model.name openai/tsubasa-pro`. The `openai/` prefix selects
LiteLLM's compatible transport; the wire model ID is the Tsubasa alias. The
request sends the prompt and Tsubasa key to `api.tsubasa.sh`.

Keep the missing-key guard. SWE-agent returns no explicit key if the named
environment variable is absent, allowing LiteLLM to use an unrelated ambient
OpenAI credential. The shell guard prevents that dispatch.

The overlay disables the example demonstration, reserves 4,096 tokens for
output, and sets a 28,672-token input limit within the combined 32,768-token
window. `completion_kwargs.max_tokens` is required to send the output cap;
the model metadata field alone does not send it for this transport. The
thought/action parser uses textual command descriptions rather than API tool
schemas. This remains an agent configuration that can execute commands;
command execution and repair quality have not been qualified.

The cost registry uses the Tsubasa catalog rates recorded September 28, 2026.
SWE-agent's local dollar estimate and call limits remain enabled. They are
checked after a request, so they are not a billing guarantee or a strict
pre-dispatch spending ceiling. Confirm current rates before relying on the
estimate.

Controlled checks loaded the exact overlay through the native configuration
merge, generated the stock thought/action command documentation, rendered the
native system and task templates, and used SWE-agent's actual model client.
Both aliases decoded JSON text, preserved a short follow-up history, recorded
a positive cost, and propagated HTTP 401. Six captured requests passed the
actual Tsubasa schema and context check before the loopback fixture replied.
The largest input estimate was 8,154 tokens plus 4,096 output. The fixture used
synthetic credentials and a synthetic environment descriptor for prompt
assembly; it did not start SWE-ReX or execute commands. HOME remained inherited,
and personal files and external network were blocked.

Live inference, full CLI environment startup, parsing and executing model
commands, Docker/SWE-ReX trajectories, streaming, and long tasks remain
unqualified. A successful model-client check is not a SWE-bench result.
