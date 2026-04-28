import streamlit as st
from langchain_huggingface import HuggingFaceEmbeddings

from app.config import DEVICE, EMBEDDING_MODEL


@st.cache_resource
def get_embedder(model_name: str = EMBEDDING_MODEL) -> HuggingFaceEmbeddings:
    return HuggingFaceEmbeddings(
        model_name=model_name,
        model_kwargs={"device": DEVICE},
        encode_kwargs={"batch_size": 8, "normalize_embeddings": True},
    )
