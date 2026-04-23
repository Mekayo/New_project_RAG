from typing import Dict, List, Optional, Tuple

from langchain_core.documents import Document

from app.config import TOP_K_RESULTS
from app.retrieval.vectorstore import load_vectorstore


def get_retriever(k: int = TOP_K_RESULTS, filter_dict: Optional[Dict] = None):
    db = load_vectorstore()
    kwargs = {"k": k}
    if filter_dict:
        kwargs["filter"] = filter_dict
    return db.as_retriever(search_kwargs=kwargs)


def similarity_search_with_scores(query: str, k: int = TOP_K_RESULTS) -> List[Tuple[Document, float]]:
    db = load_vectorstore()
    return db.similarity_search_with_score(query, k=k)
