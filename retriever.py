from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings


def build(docs):
    return Chroma.from_documents(docs, OpenAIEmbeddings())


def search(db, q):
    return db.similarity_search(q, k=4)
