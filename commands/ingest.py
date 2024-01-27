from langchain_community.document_loaders import UnstructuredHTMLLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from langchain_community.vectorstores.redis import Redis
import os


load_dotenv()
API_KEY=os.getenv('OPENAI_API_KEY')
REDIS=os.getenv("REDIS_URL")



print("preparing to load html files")
loader = UnstructuredHTMLLoader("../data/Salisbury University - Wikipedia.html")

data=loader.load()
print("html loading complete")


text_splitter = RecursiveCharacterTextSplitter(
    # Set a really small chunk size, just to show.
    chunk_size=2000,
    chunk_overlap=30,
    length_function=len,
    is_separator_regex=False,
)
print("beginning document splitting")
documents=text_splitter.split_documents(data)
print("documents have finished being split")

embeddings_model = OpenAIEmbeddings(openai_api_key=API_KEY)
print("embeddings fetched")
Redis.drop_index(
    index_name="su_data",
    delete_documents=True,
    redis_url=REDIS,
)

print("old data droped")
rds = Redis.from_documents(
    documents,
    embeddings_model,
    redis_url=REDIS,
    index_name="su_data",
)
print("new data loaded to redis")
rds.write_schema("redis_schema.yaml")
print("redis schema written")
print("data ingestion completed")







