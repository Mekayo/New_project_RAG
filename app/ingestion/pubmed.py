import time
from typing import List

from Bio import Entrez
from langchain_core.documents import Document

from app.config import NCBI_API_KEY, NCBI_EMAIL
from app.ingestion.chunker import chunk_documents
from app.retrieval.vectorstore import add_to_vectorstore, create_vectorstore

Entrez.email = NCBI_EMAIL
if NCBI_API_KEY:
    Entrez.api_key = NCBI_API_KEY


def search_pubmed(query: str, max_results: int = 10) -> List[Document]:
    handle = Entrez.esearch(db="pubmed", term=query, retmax=max_results, sort="relevance")
    record = Entrez.read(handle)
    handle.close()
    pmids = record.get("IdList", [])
    if not pmids:
        return []

    batch_delay = 0.12 if NCBI_API_KEY else 0.35
    fetch_handle = Entrez.efetch(db="pubmed", id=",".join(pmids), rettype="abstract", retmode="xml")
    fetched = Entrez.read(fetch_handle)
    fetch_handle.close()
    time.sleep(batch_delay)

    docs: List[Document] = []
    for article in fetched.get("PubmedArticle", []):
        medline = article.get("MedlineCitation", {})
        article_data = medline.get("Article", {})
        pmid = str(medline.get("PMID", ""))
        title = " ".join(article_data.get("ArticleTitle", "").split())
        abstract_section = article_data.get("Abstract", {}).get("AbstractText", [])
        abstract = " ".join(str(x) for x in abstract_section).strip()
        if not abstract:
            continue
        authors = []
        for author in article_data.get("AuthorList", []):
            last_name = author.get("LastName", "")
            initials = author.get("Initials", "")
            full_name = f"{last_name} {initials}".strip()
            if full_name:
                authors.append(full_name)
        journal = article_data.get("Journal", {}).get("Title", "")
        pub_date = article_data.get("Journal", {}).get("JournalIssue", {}).get("PubDate", {})
        pub_date_str = " ".join(str(v) for v in pub_date.values() if v)
        mesh_terms = [
            str(mesh.get("DescriptorName", ""))
            for mesh in medline.get("MeshHeadingList", [])
            if mesh.get("DescriptorName")
        ]
        mesh_terms_str = ", ".join(mesh_terms)
        docs.append(
            Document(
                page_content=abstract,
                metadata={
                    "source": "pubmed",
                    "query": query,
                    "title": title,
                    "authors": ", ".join(authors),
                    "journal": journal,
                    "pmid": pmid,
                    "date": pub_date_str,
                    "mesh_terms": mesh_terms_str,
                    "url": f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/",
                },
            )
        )
    return docs


def ingest_pubmed_results(query: str, max_results: int = 10) -> int:
    documents = search_pubmed(query, max_results=max_results)
    if not documents:
        return 0
    chunks = chunk_documents(documents)
    try:
        add_to_vectorstore(chunks)
    except Exception:
        create_vectorstore(chunks)
    return len(chunks)
