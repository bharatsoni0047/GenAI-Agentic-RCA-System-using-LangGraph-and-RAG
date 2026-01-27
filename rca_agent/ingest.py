from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from rca_agent.config import embeddings


def ingest():
    loader = TextLoader("data/error_logs.txt")
    docs = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )
    chunks = splitter.split_documents(docs)

    db = Chroma(
        persist_directory="chroma_db",
        embedding_function=embeddings
    )
    db.add_documents(chunks)
    db.persist()

if __name__ == "__main__":
    ingest()