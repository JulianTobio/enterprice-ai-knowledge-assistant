import os
from dotenv import load_dotenv

load_dotenv()

API_PREFIX = "/api"
PROJECT_TITLE = os.getenv("PROJECT_NAME")
LLM_MODEL_NAME = os.getenv("LLM_MODEL_NAME")
DOCUMENTS_PATH = os.getenv("DOCUMENTS_FOLDER")
SQL_CONNECTION_STRING = os.getenv("SQL_STRING")
QUEUE_HOST = os.getenv("QUEUE_HOST")
QUEUE_PORT = int(os.getenv("QUEUE_PORT"))
QUEUE_NAME = os.getenv("QUEUE_NAME")
CHROMA_DB_HOST = os.getenv("CHROMA_DB_HOST")
CHROMA_DB_PORT = int(os.getenv("CHROMA_DB_PORT"))
CHROMA_DB_COLLECTION = os.getenv("CHROMA_DB_COLLECTION")
OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL")