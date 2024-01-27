from operator import itemgetter
from typing import List, Tuple
from dotenv import load_dotenv
from fastapi import FastAPI
from langchain.chat_models import ChatOpenAI
from langchain.embeddings import OpenAIEmbeddings
from langchain.prompts import ChatPromptTemplate
from langchain.prompts.prompt import PromptTemplate
from langchain.schema import format_document
from langchain.schema.output_parser import StrOutputParser
from langchain.schema.runnable import RunnableMap, RunnablePassthrough
from langchain.vectorstores import FAISS

from langserve import add_routes
from langserve.pydantic_v1 import BaseModel, Field
from langchain_community.vectorstores.redis import Redis
import os


_TEMPLATE = """
Please respond as a friendly and intelligent admissions advisor for salisbury university. you may use the below context to answer the question if you don't have information based on the context provided make an educated guess. tactfully redirect the conversation to salisbury univeristy if the question was not about salisbury univeristy. 
Please answer in the same language the question was asked in. Please consider the chat history when answering

Chat History:
{chat_history}
Follow Up Input: {question}
Standalone question:"""
CONDENSE_QUESTION_PROMPT = PromptTemplate.from_template(_TEMPLATE)

ANSWER_TEMPLATE = """Please respond as a friendly and intelligent admissions advisor for salisbury university. you may use the below context to answer the question if you don't have information based on the context provided make an educated guess. tactfully redirect the conversation to salisbury univeristy if the question was not about salisbury univeristy. 
Please answer in the same language the question was asked in.
{context}

Question: {question}
"""
ANSWER_PROMPT = ChatPromptTemplate.from_template(ANSWER_TEMPLATE)

DEFAULT_DOCUMENT_PROMPT = PromptTemplate.from_template(template="{page_content}")

def _format_chat_history(chat_history: List[Tuple]) -> str:
    """Format chat history into a string."""
    buffer = ""
    for dialogue_turn in chat_history:
        human = "Human: " + dialogue_turn[0]
        ai = "Assistant: " + dialogue_turn[1]
        buffer += "\n" + "\n".join([human, ai])
    return buffer

load_dotenv()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
REDIS_URL = os.getenv('REDIS_URL')
# os.environ["AZURE_OPENAI_API_KEY"] = os.getenv('AZURE_OPENAI_API_KEY')
# os.environ["AZURE_OPENAI_ENDPOINT"] = os.getenv('AZURE_OPENAI_ENDPOINT')
# embeddings_model = AzureOpenAIEmbeddings(openai_api_version="2023-05-15",azure_deployment="embeddings")
embeddings_model = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)

new_rds = Redis.from_existing_index(
    embeddings_model,
    index_name="su_data",
    redis_url=REDIS_URL,
    schema="redis_schema.yaml",
)
retriever = new_rds.as_retriever(search_type="similarity", search_kwargs={"k": 6})

_inputs = RunnableMap(
    standalone_question=RunnablePassthrough.assign(
        chat_history=lambda x: _format_chat_history(x["chat_history"])
    )
    | CONDENSE_QUESTION_PROMPT
    | ChatOpenAI(temperature=1)
    | StrOutputParser(),
)
_context = {
    "context": itemgetter("standalone_question") | retriever,
    "question": lambda x: x["standalone_question"],
}


# User input
class ChatHistory(BaseModel):
    """Chat history with the bot."""

    chat_history: List[Tuple[str, str]] = Field(
        ...,
        extra={"widget": {"type": "chat", "input": "question"}},
    )
    question: str


conversational_qa_chain = (
    _inputs | _context | ANSWER_PROMPT | ChatOpenAI() | StrOutputParser()
)
chain = conversational_qa_chain.with_types(input_type=ChatHistory)

app = FastAPI(
    title="LangChain Server",
    version="1.0",
    description="Spin up a simple api server using Langchain's Runnable interfaces",
)
# Adds routes to the app for using the chain under:
# /invoke
# /batch
# /stream
add_routes(app, chain, enable_feedback_endpoint=True,path="/su")

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8000)