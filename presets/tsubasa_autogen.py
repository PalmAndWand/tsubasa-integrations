"""Bounded text setup for AutoGen's existing OpenAI-compatible client."""
import os

from autogen_core.models import ModelFamily
from autogen_ext.models.openai import OpenAIChatCompletionClient


def create_tsubasa_client(model="tsubasa-fast", *, base_url="https://api.tsubasa.sh/v1"):
    if model not in ("tsubasa-fast", "tsubasa-pro"):
        raise ValueError("Select tsubasa-fast or tsubasa-pro")
    return OpenAIChatCompletionClient(
        model=model,
        base_url=base_url,
        api_key=os.environ["TSUBASA_API_KEY"],
        max_tokens=2048,
        max_retries=0,
        timeout=30,
        include_name_in_message=False,
        model_info={
            "vision": False,
            "function_calling": False,
            "json_output": False,
            "structured_output": False,
            "family": ModelFamily.UNKNOWN,
        },
    )
