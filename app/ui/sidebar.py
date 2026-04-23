import streamlit as st

from app.config import TOP_K_RESULTS
from app.ingestion.chunker import chunk_documents
from app.ingestion.loader import load_documents, load_uploaded_files
from app.ingestion.pubmed import ingest_pubmed_results
from app.retrieval.vectorstore import add_to_vectorstore, create_vectorstore, get_collection_stats


def render_sidebar():
    st.sidebar.header("Document Management")
    uploaded_files = st.sidebar.file_uploader(
        "Upload PDF files",
        type=["pdf"],
        accept_multiple_files=True,
    )

    if st.sidebar.button("Index Documents", use_container_width=True):
        try:
            docs = []
            if uploaded_files:
                docs.extend(load_uploaded_files(uploaded_files))
            else:
                docs.extend(load_documents())
            if docs:
                chunks = chunk_documents(docs)
                try:
                    add_to_vectorstore(chunks)
                except Exception:
                    create_vectorstore(chunks)
                st.sidebar.success(f"Indexed {len(chunks)} chunks")
            else:
                st.sidebar.warning("No documents found")
        except Exception as exc:
            st.sidebar.error(f"Indexing failed: {exc}")

    st.sidebar.divider()
    st.sidebar.subheader("PubMed Search")
    pubmed_query = st.sidebar.text_input("Medical topic")
    max_results = st.sidebar.slider("Max PubMed papers", min_value=1, max_value=30, value=10)
    if st.sidebar.button("Fetch + Index PubMed", use_container_width=True):
        if pubmed_query.strip():
            try:
                chunk_count = ingest_pubmed_results(pubmed_query.strip(), max_results=max_results)
                st.sidebar.success(f"Indexed {chunk_count} PubMed chunks")
            except Exception as exc:
                st.sidebar.error(f"PubMed indexing failed: {exc}")
        else:
            st.sidebar.warning("Enter a topic first")

    st.sidebar.divider()
    st.sidebar.subheader("Generation Settings")
    temperature = st.sidebar.slider("Temperature", min_value=0.0, max_value=1.0, value=0.1, step=0.05)
    top_k = st.sidebar.slider("Top-K", min_value=1, max_value=15, value=TOP_K_RESULTS)

    st.sidebar.divider()
    st.sidebar.subheader("Collection Stats")
    if st.sidebar.button("Refresh Stats", use_container_width=True):
        st.session_state["stats_refresh"] = True
    stats = {"count": 0, "sources": {}}
    try:
        stats = get_collection_stats()
    except Exception:
        pass
    st.sidebar.write(f"Chunks: {stats.get('count', 0)}")
    st.sidebar.json(stats.get("sources", {}))

    return {"temperature": temperature, "top_k": top_k}
