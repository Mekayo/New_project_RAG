from langchain_groq import ChatGroq

from app.config import GROQ_API_KEY, LLM_MODEL, validate_required_settings


def get_llm(temperature: float = 0.1) -> ChatGroq:
    validate_required_settings()
    return ChatGroq(
        model_name=LLM_MODEL,
        temperature=temperature,
        api_key=GROQ_API_KEY,
    )
