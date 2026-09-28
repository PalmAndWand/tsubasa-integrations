import os
from llama_index.llms.openai_like import OpenAILike

tsubasa = OpenAILike(
    model="tsubasa-pro",
    api_base="https://api.tsubasa.sh/v1",
    api_key=os.environ["TSUBASA_API_KEY"],
    context_window=32768,
    max_tokens=128,
    is_chat_model=True,
    is_function_calling_model=False,
)

if __name__ == "__main__":
    print(tsubasa.complete("Explain binary search in one sentence."))
