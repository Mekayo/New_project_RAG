import os

import torch
from dotenv import load_dotenv

load_dotenv()


def _strip_quotes(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and ((value[0] == value[-1] == '"') or (value[0] == value[-1] == "'")):
        return value[1:-1].strip()
    return value


GROQ_API_KEY = _strip_quotes(os.getenv("GROQ_API_KEY", ""))

NCBI_API_KEY = os.getenv("NCBI_API_KEY", "").strip() or None
NCBI_EMAIL = os.getenv("NCBI_EMAIL", "user@example.com").strip()
VECTOR_DB_PATH = os.getenv("VECTOR_DB_PATH", "./data/chroma_db")
CHUNK_SIZE = int(os.getenv("CHUNK_SIZE", "512"))
CHUNK_OVERLAP = int(os.getenv("CHUNK_OVERLAP", "50"))
TOP_K_RESULTS = int(os.getenv("TOP_K_RESULTS", "5"))
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "all-MiniLM-L6-v2")
LLM_MODEL = os.getenv("LLM_MODEL", "llama-3.3-70b-versatile").strip()

configured_device = os.getenv("DEVICE", "cuda").lower()
if configured_device == "cuda" and torch.cuda.is_available():
    DEVICE = "cuda"
else:
    DEVICE = "cpu"


def validate_required_settings() -> None:
    if not GROQ_API_KEY:
        raise ValueError("GROQ_API_KEY is required. Set it in your .env file.")
