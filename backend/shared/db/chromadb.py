import chromadb
from app.core.config import CHROMA_DB_HOST, CHROMA_DB_PORT, CHROMA_DB_COLLECTION

def get_collection():
    client = chromadb.HttpClient(host=CHROMA_DB_HOST, port=int(CHROMA_DB_PORT)) 
    collection = client.get_or_create_collection(name=CHROMA_DB_COLLECTION)
    return collection