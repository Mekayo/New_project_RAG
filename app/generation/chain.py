from langchain.chains import LLMChain, RetrievalQA
from langchain_core.documents import Document

from app.config import TOP_K_RESULTS
from app.generation.llm import get_llm
from app.generation.prompts import RAG_PROMPT, SUMMARIZE_PROMPT
from app.retrieval.retriever import get_retriever


def build_rag_chain(top_k: int = TOP_K_RESULTS, temperature: float = 0.1) -> RetrievalQA:
    llm = get_llm(temperature=temperature)
    retriever = get_retriever(k=top_k)
    return RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever,
        return_source_documents=True,
        chain_type_kwargs={"prompt": RAG_PROMPT},
    )


def build_summarize_chain(temperature: float = 0.1) -> LLMChain:
    llm = get_llm(temperature=temperature)
    return LLMChain(llm=llm, prompt=SUMMARIZE_PROMPT)


def summarize_documents(documents: list[Document], temperature: float = 0.1) -> str:
    context = "\n\n".join(doc.page_content for doc in documents)
    chain = build_summarize_chain(temperature=temperature)
    return chain.run(context=context)
