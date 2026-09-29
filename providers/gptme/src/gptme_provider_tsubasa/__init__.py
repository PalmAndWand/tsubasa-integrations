"""Tsubasa metadata for gptme's native OpenAI-compatible transport."""

from gptme.llm.models import ModelMeta, ProviderPlugin

provider = ProviderPlugin(
    name="tsubasa",
    api_key_env="TSUBASA_API_KEY",
    base_url="https://api.tsubasa.sh/v1",
    models=[
        ModelMeta(
            provider="unknown",
            model=f"tsubasa/{model}",
            context=32_768,
            max_output=max_output,
            price_input=price_input,
            price_output=price_output,
            supports_streaming=False,
            supports_mid_system=False,
        )
        for model, max_output, price_input, price_output in (
            ("tsubasa-fast", 8_192, 0.20, 1.00),
            ("tsubasa-pro", 16_384, 0.50, 4.00),
        )
    ],
)
