from pathlib import Path
from typing import Dict, List

from langchain_chroma import Chroma
from langchain_core.documents import Document

from app.config import VECTOR_DB_PATH
from app.ingestion.embedder import get_embedder
from app.ingestion.metadata import normalize_document_metadata

COLLECTION_NAME = "healthcare_research"


def create_vectorstore(chunks: List[Document]) -> Chroma:
    Path(VECTOR_DB_PATH).mkdir(parents=True, exist_ok=True)
    normalize_document_metadata(chunks)
    embedding = get_embedder()
    return Chroma.from_documents(
        documents=chunks,
        embedding=embedding,
        persist_directory=VECTOR_DB_PATH,
        collection_name=COLLECTION_NAME,
    )


def load_vectorstore() -> Chroma:
    Path(VECTOR_DB_PATH).mkdir(parents=True, exist_ok=True)
    embedding = get_embedder()
    return Chroma(
        persist_directory=VECTOR_DB_PATH,
        embedding_function=embedding,
        collection_name=COLLECTION_NAME,
    )


def add_to_vectorstore(chunks: List[Document]) -> Chroma:
    normalize_document_metadata(chunks)
    db = load_vectorstore()
    db.add_documents(chunks)
    return db


def get_collection_stats() -> Dict[str, object]:
    db = load_vectorstore()
    collection = db.get()
    metadatas = collection.get("metadatas", [])
    source_counts: Dict[str, int] = {}
    for metadata in metadatas:
        source = metadata.get("source", "unknown")
        source_counts[source] = source_counts.get(source, 0) + 1
    return {"count": len(collection.get("ids", [])), "sources": source_counts}
