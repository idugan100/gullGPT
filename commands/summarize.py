from dotenv import load_dotenv
import os
from langchain_openai import ChatOpenAI
from langchain_openai import AzureChatOpenAI
from langchain.prompts.chat import ChatPromptTemplate
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from fastapi import FastAPI
from langserve import add_routes
from fastapi.middleware.cors import CORSMiddleware

load_dotenv()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
os.environ["AZURE_OPENAI_API_KEY"] = os.getenv('AZURE_OPENAI_API_KEY')
os.environ["AZURE_OPENAI_ENDPOINT"] = os.getenv('AZURE_OPENAI_ENDPOINT')

# chat_model = AzureChatOpenAI(openai_api_version="2023-05-15",azure_deployment="chat")
chat_model = ChatOpenAI(openai_api_key=OPENAI_API_KEY, temperature=0)

template = """
rewrite the below dialoge in half the words.
Transcript:
  {input}"""

chat_prompt = ChatPromptTemplate.from_messages([
    ("system", template),
])

chain = (  chat_prompt
        | chat_model
        | StrOutputParser()
        )

app = FastAPI(
    title="LangChain Server",
    version="1.0",
    description="A simple api server using Langchain's Runnable interfaces",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

add_routes(
    app,
    chain,
    path="/summarize",
)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8002)