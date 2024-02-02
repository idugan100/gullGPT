from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
import os
from langchain_community.vectorstores.redis import Redis
from langchain_openai import ChatOpenAI
from langchain_openai import AzureChatOpenAI
from langchain.prompts.chat import ChatPromptTemplate
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from fastapi import FastAPI
from langserve import add_routes
from fastapi.middleware.cors import CORSMiddleware
from langchain.retrievers.multi_query import MultiQueryRetriever
from langchain.retrievers import ContextualCompressionRetriever
from langchain.retrievers.document_compressors import LLMChainExtractor

model = input("What model do you want to use? (3.5, 4, 4.5): ")
highIQ = input("Do you want to run this in highIQ mode? This will make the service much slower (y/n): ")
model_list ={"3.5":"gpt-3.5-turbo","4":"gpt-4","4.5":"gpt-4-0125-preview"}

load_dotenv()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
REDIS_URL = os.getenv('REDIS_URL')
os.environ["AZURE_OPENAI_API_KEY"] = os.getenv('AZURE_OPENAI_API_KEY')
os.environ["AZURE_OPENAI_ENDPOINT"] = os.getenv('AZURE_OPENAI_ENDPOINT')
embeddings_model = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)

new_rds = Redis.from_existing_index(
    embeddings_model,
    index_name="su_data",
    redis_url=REDIS_URL,
    schema="redis_schema.yaml",
)

retriever = new_rds.as_retriever(search_type="similarity", search_kwargs={"k": 5})

chat_model = ChatOpenAI(openai_api_key=OPENAI_API_KEY, model=model_list[model])
compressor = LLMChainExtractor.from_llm(chat_model)

if highIQ=='y':
    multi_query_retriver = MultiQueryRetriever.from_llm(
        retriever=retriever, llm=chat_model
    )

    compression_retriever = ContextualCompressionRetriever(
        base_compressor=compressor, base_retriever=multi_query_retriver
    )
    final_retriever = compression_retriever
else:
    final_retriever = retriever

template = """
Please respond as a friendly and intelligent admissions advisor for salisbury university. 
you may use the below contex to answer the question 
if you don't have information based on the contex provided make an educated guess. 
tactfully redirect the conversation to salisbury univeristy if the question was not about salisbury univeristy. 
Please answer in the same language the question was asked in. Do not use the phrase: salisbury admissions counselor  in your repsonse
Consider the previous message history or summary of history in your response. Keep response under 100 words. Context:{context}  {input}"""

chat_prompt = ChatPromptTemplate.from_messages([
    ("system", template),
])

chain = ({"context": final_retriever, "input": RunnablePassthrough(),}
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
    path="/chat/su",
)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8000)