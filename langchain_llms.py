import os

from dotenv import load_dotenv

from langchain_anthropic import ChatAnthropic
#from langchain_ollama import ChatOllama
#from langchain_openai import ChatOpenAi

load_dotenv()
llm = ChatAnthropic(model_name=os.getenv("MODEL_NAME"),api_key=os.getenv("API_KEY")
                    , temperature=0, timeout=180, stop=120)
response = llm.invoke("Can you explain what a movie is?")
print("llm response: ", response)

# def main():
#     print("Hello from langchain-basics!")
#
#
# if __name__ == "__main__":
#     main()
