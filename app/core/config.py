import os
from dotenv import load_dotenv

load_dotenv()

API_PREFIX = "/api"
PROJECT_TITLE = os.getenv("PROJECT_NAME")
LLM_MODEL_NAME = os.getenv("LLM_MODEL_NAME")