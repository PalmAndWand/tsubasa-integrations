# DSPy

Install `dspy==3.4.0` in an isolated Python environment and set
`TSUBASA_API_KEY` using your normal secret-management method. Then run:

```sh
: "${TSUBASA_API_KEY:?Set TSUBASA_API_KEY}"
python presets/tsubasa_dspy.py
```

The [example](../presets/tsubasa_dspy.py) registers Tsubasa through DSPy’s
existing `lm15` provider declaration API and makes one text call. It sends
prompts and the dedicated key to `https://api.tsubasa.sh/v1`. Fast is the
example default; replace `tsubasa/tsubasa-fast` with `tsubasa/tsubasa-pro` for
Pro. Keep the same registration available when loading a saved program.

The output cap is 256 tokens. Both models share a 32,768-token context window;
input, history and output must fit together. Model tool, reasoning and
response-schema capabilities remain unstated.

DSPy 3.4.0 completed four controlled native text requests: both aliases through
this declared-provider API and separately through its existing generic LiteLLM
route. All four passed Tsubasa’s request schema and context checks. Streaming,
invalid-key handling, optimizers, saved-program loading, tool execution and
live inference were not qualified. This is an external configuration example,
not an upstream built-in provider.
