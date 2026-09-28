"""Bounded text setup using Semantic Kernel's supplied OpenAI client route."""
import os

from openai import AsyncOpenAI
from semantic_kernel.connectors.ai.open_ai import (
    OpenAIChatCompletion,
    OpenAIChatPromptExecutionSettings,
)


def create_tsubasa_service(model="tsubasa-fast", *, base_url="https://api.tsubasa.sh/v1"):
    if model not in ("tsubasa-fast", "tsubasa-pro"):
        raise ValueError("Select tsubasa-fast or tsubasa-pro")
    client = AsyncOpenAI(
        api_key=os.environ["TSUBASA_API_KEY"],
        base_url=base_url,
        max_retries=0,
        timeout=30,
    )
    return OpenAIChatCompletion(ai_model_id=model, service_id="tsubasa", async_client=client)


def text_settings():
    return OpenAIChatPromptExecutionSettings(max_tokens=2048, number_of_responses=1)
