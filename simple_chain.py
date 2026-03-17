import os

from langchain_classic.prompts import PromptTemplate
from langchain_anthropic import ChatAnthropic
from langchain.chains import LLMChain

from dotenv import load_dotenv

load_dotenv()

prompt = PromptTemplate(input_variables=["stock_name"],
                        template="Can you provide fundamental analysis for the stock {stock_name}")

chat_model = ChatAnthropic(model_name=os.getenv("MODEL_NAME"), api_key=os.getenv("API_KEY")
                           ,temperature=0, timeout=180, stop=120)
