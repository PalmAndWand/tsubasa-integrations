"""Custom registration for DSPy 3.4.0; not an upstream native entry."""
import dspy
from dspy.lm15 import (
    AccessPolicy, EndpointSupport, OpenAIChatCompat, ProviderDefinition, register_provider,
)

register_provider(ProviderDefinition.chat(
    AccessPolicy(
        provider="tsubasa", base_url="https://api.tsubasa.sh/v1",
        env_keys=("TSUBASA_API_KEY",), auth_modes=("bearer",), auth_scheme=("bearer",),
        supports=EndpointSupport(complete=True, stream=True),
    ),
    compat=OpenAIChatCompat(max_tokens_field="max_tokens"),
))
# Tool/reasoning/schema model capabilities are deliberately left unstated.
lm = dspy.LM("tsubasa/tsubasa-fast", engine="lm15", max_tokens=256, cache=False)
print(lm("Hello"))  # tsubasa/tsubasa-pro is the other public alias.
