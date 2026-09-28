"""Tsubasa model provider for Hermes; live qualification is pending."""

from providers import register_provider
from providers.base import ProviderProfile

register_provider(ProviderProfile(
    name="tsubasa",
    display_name="Tsubasa",
    description="Hosted OpenAI-compatible inference for developer tools.",
    signup_url="https://tsubasa.sh/api-keys",
    env_vars=("TSUBASA_API_KEY",),
    base_url="https://api.tsubasa.sh/v1",
    auth_type="api_key",
    supports_vision=False,
    supports_vision_tool_messages=False,
    model_capabilities={
        "tsubasa-fast": {"context_window": 32768, "supports_tools": False, "supports_vision": False, "supports_reasoning": False},
        "tsubasa-pro": {"context_window": 32768, "supports_tools": False, "supports_vision": False, "supports_reasoning": False},
    },
))
