import os
from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIChatModel
from pydantic_ai.providers.openai import OpenAIProvider

tsubasa = Agent(OpenAIChatModel(
    "tsubasa-pro",
    provider=OpenAIProvider(base_url="https://api.tsubasa.sh/v1", api_key=os.environ["TSUBASA_API_KEY"]),
), model_settings={"max_tokens": 128})

if __name__ == "__main__":
    print(tsubasa.run_sync("Explain binary search in one sentence.").output)
