from langchain.prompts import PromptTemplate

RAG_PROMPT = PromptTemplate(
    input_variables=["context", "question"],
    template=(
        "You are a healthcare research assistant.\n"
        "Answer only from the provided context.\n"
        "If the context is insufficient, respond with: I don't have enough information.\n"
        "Include source citations with title and PMID where available.\n\n"
        "Context:\n{context}\n\n"
        "Question:\n{question}\n\n"
        "Answer:"
    ),
)

SUMMARIZE_PROMPT = PromptTemplate(
    input_variables=["context"],
    template=(
        "Summarize the following medical research context as concise bullet points.\n"
        "Focus on findings, methods, population, and limitations.\n\n"
        "Context:\n{context}\n\n"
        "Summary:"
    ),
)
