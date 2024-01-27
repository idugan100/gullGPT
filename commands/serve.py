from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
import os
from langchain_community.vectorstores.redis import Redis
from langchain_openai import ChatOpenAI
from langchain_openai import OpenAI
from langchain.prompts.chat import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from fastapi import FastAPI
from langserve import add_routes

load_dotenv()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
REDIS_URL = os.getenv('REDIS_URL')
embeddings_model = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)

new_rds = Redis.from_existing_index(
    embeddings_model,
    index_name="su_data",
    redis_url=REDIS_URL,
    schema="redis_schema.yaml",
)

retriever = new_rds.as_retriever(search_type="similarity", search_kwargs={"k": 4})

chat_model = ChatOpenAI(openai_api_key=OPENAI_API_KEY)

template = "Please resopond as a friendly and intelligent admissions advisor for university of maryland. you may use the below contex to answer the question if you don't have information based on the contex provided make an educated guess. tactfully redirect the conversation to the univeristy of maryland if the question was not about the university of maryland. Please answer in the same language the question was asked in. Context:{context} Question: {question}"

chat_prompt = ChatPromptTemplate.from_messages([
    ("system", template),
])

chain = ({"context": retriever, "question": RunnablePassthrough()}
        | chat_prompt
        | chat_model
        | StrOutputParser()
        )

app = FastAPI(
    title="LangChain Server",
    version="1.0",
    description="A simple api server using Langchain's Runnable interfaces",
)

add_routes(
    app,
    chain,
    path="/su",
)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8000)