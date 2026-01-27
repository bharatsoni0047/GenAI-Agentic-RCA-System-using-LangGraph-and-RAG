from langchain_community.vectorstores import Chroma
from rca_agent.config import embeddings


def get_retriever():
    db = Chroma(
        persist_directory="chroma_db",
        embedding_function=embeddings
    )
    return db.as_retriever(k=4)
