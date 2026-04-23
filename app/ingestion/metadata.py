import json
from typing import Any, Dict, List

from langchain_core.documents import Document


def normalize_metadata_value(value: Any) -> str | int | float | bool:
    if value is None:
        return ""
    if isinstance(value, (bool, int, float, str)):
        return value
    if isinstance(value, (list, tuple, set, dict)):
        return json.dumps(value, ensure_ascii=False, default=str)
    return str(value)


def normalize_document_metadata(docs: List[Document]) -> None:
    for doc in docs:
        metadata: Dict[str, Any] = dict(doc.metadata or {})
        for key, val in list(metadata.items()):
            metadata[key] = normalize_metadata_value(val)
        doc.metadata = metadata
