from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from langchain_community.vectorstores.redis import Redis
from csv_loader import get_csv_documents
import os
from langchain_community.document_loaders import DirectoryLoader
from langchain_community.document_loaders import PyPDFLoader
from datetime import datetime
from langchain.cache import InMemoryCache
from langchain_community.document_loaders.sitemap import SitemapLoader
import nest_asyncio
from langchain_community.vectorstores import SQLiteVSS
import time
import sqlite3


nest_asyncio.apply()


startTime = datetime.now()

load_dotenv()
API_KEY=os.getenv('OPENAI_API_KEY')
REDIS=os.getenv("REDIS_URL")

print("preparing to load pdf files")
pdf_loader = DirectoryLoader('../data/pdf/', loader_cls=PyPDFLoader)
pdf_documents=pdf_loader.load()
print("pdf file loading complete")

print("beginning sitemap loader")
sitemap_loader = SitemapLoader(web_path="https://www.salisbury.edu/sitemap.xml")
sitemap_loader.requests_kwargs = {"verify": False}
sitemap_loader.requests_per_second = 2
html_documents = sitemap_loader.load()
print("finished sitemap loader")

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
print(len(split_documents))
print("documents have finished being split")

embeddings_model = OpenAIEmbeddings(openai_api_key=API_KEY)

print("embeddings fetched")


connection = sqlite3.connect("../../data.db")
cursor = connection.cursor()
cursor.execute("DELETE FROM vectors")
connection.commit()
connection.close()
print("old data dropped")

for i in range(0, len(split_documents),500):
    chunk = split_documents[i:i+500]
    print(i,min(i+500,len(split_documents)))
    db = SQLiteVSS.from_documents(
        chunk,
        embeddings_model,
        table="vectors",
        db_file="../../data.db",
    )
    print("chunk inserted. waiting for timeout")
    time.sleep(60)


print("data ingestion completed in " + str(datetime.now() - startTime) + " seconds")