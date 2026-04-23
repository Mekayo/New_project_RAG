import streamlit as st

from app.generation.chain import build_rag_chain, summarize_documents
from app.retrieval.retriever import get_retriever


def _render_sources(source_documents):
    with st.expander("Sources", expanded=False):
        for idx, doc in enumerate(source_documents, start=1):
            metadata = doc.metadata
            title = metadata.get("title") or metadata.get("source", "Document")
            pmid = metadata.get("pmid")
            st.markdown(f"**{idx}. {title}**")
            if pmid:
                st.write(f"PMID: {pmid}")
            if metadata.get("url"):
                st.write(metadata["url"])
            st.caption(doc.page_content[:500] + ("..." if len(doc.page_content) > 500 else ""))


def render_chat(settings):
    if "messages" not in st.session_state:
        st.session_state.messages = []

    summarize_mode = st.toggle("Summarize mode", value=False)

    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])
            if msg.get("sources"):
                _render_sources(msg["sources"])

    user_query = st.chat_input("Ask a medical research question")
    if not user_query:
        return

    st.session_state.messages.append({"role": "user", "content": user_query})
    with st.chat_message("user"):
        st.markdown(user_query)

    with st.chat_message("assistant"):
        with st.spinner("Generating answer..."):
            try:
                if summarize_mode:
                    retriever = get_retriever(k=settings["top_k"])
                    docs = retriever.get_relevant_documents(user_query)
                    answer = summarize_documents(docs, temperature=settings["temperature"])
                    sources = docs
                else:
                    chain = build_rag_chain(top_k=settings["top_k"], temperature=settings["temperature"])
                    result = chain({"query": user_query})
                    answer = result["result"]
                    sources = result.get("source_documents", [])
            except Exception as exc:
                answer = f"Request failed: {exc}"
                sources = []
            st.markdown(answer)
            if sources:
                _render_sources(sources)

    st.session_state.messages.append({"role": "assistant", "content": answer, "sources": sources})
