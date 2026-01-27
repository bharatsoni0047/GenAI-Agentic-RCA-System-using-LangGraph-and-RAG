from langchain_community.chat_models import ChatOllama
from langchain_community.embeddings import OllamaEmbeddings

MODEL_NAME = "phi3"

llm = ChatOllama(
    model=MODEL_NAME,
    temperature=0
)

embeddings = OllamaEmbeddings(
    model=MODEL_NAME
)
