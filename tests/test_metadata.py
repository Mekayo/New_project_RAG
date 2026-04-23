from langchain_core.documents import Document

from app.ingestion.metadata import normalize_document_metadata


def test_normalize_list_metadata_to_string():
    docs = [Document(page_content="x", metadata={"k": [1, 2]})]
    normalize_document_metadata(docs)
    assert isinstance(docs[0].metadata["k"], str)
