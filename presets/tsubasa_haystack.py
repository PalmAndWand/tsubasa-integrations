from haystack.components.generators.chat import OpenAIChatGenerator
from haystack.dataclasses import ChatMessage
from haystack.utils import Secret

tsubasa = OpenAIChatGenerator(
    api_key=Secret.from_env_var("TSUBASA_API_KEY"),
    api_base_url="https://api.tsubasa.sh/v1",
    model="tsubasa-pro",
    generation_kwargs={"max_tokens": 128},
)

if __name__ == "__main__":
    result = tsubasa.run(messages=[ChatMessage.from_user("Explain binary search in one sentence.")])
    print(result["replies"][0].text)
