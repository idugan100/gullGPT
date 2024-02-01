from langchain_community.document_loaders import UnstructuredHTMLLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from langchain_community.vectorstores.redis import Redis
from csv_loader import get_csv_documents
import os
from langchain_openai import AzureOpenAIEmbeddings
from langchain_community.document_loaders import DirectoryLoader
from langchain_community.document_loaders import PyPDFLoader
from datetime import datetime

startTime = datetime.now()

load_dotenv()
API_KEY=os.getenv('OPENAI_API_KEY')
AZURE_OPENAI_API_KEY= os.getenv('AZURE_OPENAI_API_KEY')
AZURE_OPENAI_ENDPOINT= os.getenv('AZURE_OPENAI_ENDPOINT')
REDIS=os.getenv("REDIS_URL")

print("preparing to load pdf files")
pdf_loader = DirectoryLoader('../data/pdf/', loader_cls=PyPDFLoader)
pdf_documents=pdf_loader.load()
print("pdf file loading complete")

print("preparing to load html files")
html_loader = DirectoryLoader('../data/html/', loader_cls=UnstructuredHTMLLoader)
html_documents = html_loader.load()
print("html loading complete")

print("preparing to load csv files")
csv_documents = get_csv_documents()
print("csv loading complete")

documents = [
    *pdf_documents,
    *html_documents,
    *csv_documents
]

print("beginning document splitting")
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=2000,
    chunk_overlap=200,
    length_function=len,
    is_separator_regex=False,
)
split_documents=text_splitter.split_documents(documents)
print("documents have finished being split")

embeddings_model = OpenAIEmbeddings(openai_api_key=API_KEY)
# embeddings_model = AzureOpenAIEmbeddings(
#     azure_deployment="embeddings",
#     openai_api_version="2023-05-15",
# )
print("embeddings fetched")

Redis.drop_index(
    index_name="su_data",
    delete_documents=True,
    redis_url=REDIS,
)
print("old data droped")

rds = Redis.from_documents(
    split_documents,
    embeddings_model,
    redis_url=REDIS,
    index_name="su_data",
)
print("new data loaded to redis")

rds.write_schema("redis_schema.yaml")
print("redis schema written")

print("data ingestion completed in " + str(datetime.now() - startTime) + " seconds")