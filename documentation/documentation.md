## Data
- the data folder is where all the various types of data used in our application is stored including html files, pdf files, and csv files

## Commands 
- the commands folder hosts the scripts and services used to run and support gullGPT
- update.py
    - this command rescrapes all the html and pdf files in our data folder so  we  have the latest information stored
- ingest.py
    - this command takes all the files in the data folder, splits them into like sized documents, gets the Azure OpenAI vector embedding and inserts them into our Redis vector store 
- summarize.py
    - this command runs Langserve - a Langchain based REST api and exposes end points that allow us to summarize and condense chat histories
- serve.py
    - this command runs another Langserve service that takes in a summarized chat history and a questions and provided a response using our custom prompt template and our Redis backed RAG system
- redis_schema.yaml
    - this file provides a common definition of how the Redis vector store is structed for all the services to use when connecting to it

## Frontend
- index.html
    - this file contains the client which makes api calls to both the summarize and serve services to provide a smooth user experience

## Documentation
- files and folders explaining our solution, architecture, and costs
