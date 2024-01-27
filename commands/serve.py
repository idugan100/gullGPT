from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
import os
from langchain_community.vectorstores.redis import Redis
from langchain_openai import ChatOpenAI
from langchain_openai import AzureChatOpenAI
from langchain.prompts.chat import ChatPromptTemplate
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough, RunnableLambda
from fastapi import FastAPI
from langserve import add_routes
from langchain_openai import AzureOpenAIEmbeddings
from langchain.memory import ConversationBufferMemory
from fastapi.middleware.cors import CORSMiddleware




load_dotenv()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
REDIS_URL = os.getenv('REDIS_URL')
os.environ["AZURE_OPENAI_API_KEY"] = os.getenv('AZURE_OPENAI_API_KEY')
os.environ["AZURE_OPENAI_ENDPOINT"] = os.getenv('AZURE_OPENAI_ENDPOINT')
# embeddings_model = AzureOpenAIEmbeddings(openai_api_version="2023-05-15",azure_deployment="embeddings")
embeddings_model = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)

new_rds = Redis.from_existing_index(
    embeddings_model,
    index_name="su_data",
    redis_url=REDIS_URL,
    schema="redis_schema.yaml",
)

retriever = new_rds.as_retriever(search_type="similarity", search_kwargs={"k": 6})

# chat_model = AzureChatOpenAI(openai_api_version="2023-05-15",azure_deployment="chat")
chat_model = ChatOpenAI(openai_api_key=OPENAI_API_KEY)


template = "Please respond as a friendly and intelligent admissions advisor for salisbury university. you may use the below contex to answer the question if you don't have information based on the contex provided make an educated guess. tactfully redirect the conversation to salisbury univeristy if the question was not about salisbury univeristy. Please answer in the same language the question was asked in. Consider the previous message history:{history} Context:{context} Question: {question}"

chat_prompt = ChatPromptTemplate.from_messages([
    ("system", template),
])

memory = ConversationBufferMemory(return_messages=True,output_key="ai", 
        input_key="human")

memory.save_context({"human":"my name is isaac"},{"ai":"hello isaac"})

chain = ({"context": retriever, "question": RunnablePassthrough(),"history": RunnableLambda(memory.load_memory_variables),}
        | chat_prompt
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
    path="/su",
)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8000)