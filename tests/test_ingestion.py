from langchain_core.documents import Document

from app.ingestion.chunker import chunk_documents


def test_chunk_documents_adds_metadata():
    docs = [Document(page_content="A " * 200, metadata={"source": "test"})]
    chunks = chunk_documents(docs, chunk_size=50, chunk_overlap=10)
    assert len(chunks) > 1
    assert all("chunk_index" in chunk.metadata for chunk in chunks)


def test_chunk_documents_preserve_source():
    docs = [Document(page_content="medical context", metadata={"source": "unit"})]
    chunks = chunk_documents(docs, chunk_size=20, chunk_overlap=0)
    assert chunks[0].metadata["source"] == "unit"
