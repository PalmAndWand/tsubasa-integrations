import os
from langchain_openai import ChatOpenAI

tsubasa = ChatOpenAI(
    model="tsubasa-pro",
    api_key=os.environ["TSUBASA_API_KEY"],
    base_url="https://api.tsubasa.sh/v1",
    use_responses_api=False,
    max_tokens=128,
)

if __name__ == "__main__":
    print(tsubasa.invoke("Explain binary search in one sentence.").content)
