from langchain_community.document_loaders import UnstructuredHTMLLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from langchain_community.vectorstores.redis import Redis
from langchain_community.document_loaders.csv_loader import CSVLoader
import os
from langchain_openai import AzureOpenAIEmbeddings
from langchain_community.document_loaders import DirectoryLoader
from langchain_community.document_loaders import PyPDFLoader



load_dotenv()
API_KEY=os.getenv('OPENAI_API_KEY')
os.environ["AZURE_OPENAI_API_KEY"] = os.getenv('AZURE_OPENAI_API_KEY')
os.environ["AZURE_OPENAI_ENDPOINT"] = os.getenv('AZURE_OPENAI_ENDPOINT')
REDIS=os.getenv("REDIS_URL")


print("preparing to load pdf files")
pdf_loader = DirectoryLoader('../data/pdf/', loader_cls=PyPDFLoader)
print("pdf file loading complete")

print("preparing to load html files")
html_loader = DirectoryLoader('../data/html/', loader_cls=UnstructuredHTMLLoader)
print("html loading complete")

print("preparing to load csv files")
# csv_loader = DirectoryLoader('../data/csv/', loader_cls=CSVLoader)
csv_loader1 = CSVLoader(file_path='../data/csv/classes.csv',csv_args={
    'delimiter': ',',
    'quotechar': '"',
    'fieldnames': ["description","courseNumber","departmentCode","courseTitle","avg_gpa","A_rate","B_rate","C_rate","D_rate","F_rate","Withdraw_rate","total_enrollment"]
})
csv_loader2 = CSVLoader(file_path='../data/csv/ap.csv',csv_args={
    'delimiter': ',',
    'quotechar': '"',
    'fieldnames': ['AP course', 'minimum score on ap test', 'college credits awarded','coursed granted prior to fall 2024','courses grated after fall 2024']
})
csv_loader3 = CSVLoader(file_path='../data/csv/ib.csv',csv_args={
    'delimiter': ',',
    'quotechar': '"',
    'fieldnames': ['International Baccalaureate (IB)', 'credits granted', 'courses granted']
})
csv_loader4 = CSVLoader(file_path='../data/csv/professors.csv',csv_args={
    'delimiter': ',',
    'quotechar': '"',
    'fieldnames': ["firstName","lastName","avg_gpa","total_enrollment","Withdraw_rate","A_rate","B_rate","C_rate","D_rate","F_rate","courses_taught"
]
})

print("loaded csv files")

data = [
    *html_loader.load(),
    *csv_loader1.load(),
    *csv_loader2.load(),
    *csv_loader3.load(),
    *csv_loader4.load(),
    *pdf_loader.load()
]

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=2000,
    chunk_overlap=200,
    length_function=len,
    is_separator_regex=False,
)
print("beginning document splitting")
documents=text_splitter.split_documents(data)
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
    documents,
    embeddings_model,
    redis_url=REDIS,
    index_name="su_data",
)
print("new data loaded to redis")
rds.write_schema("redis_schema.yaml")
print("redis schema written")
print("data ingestion completed")







