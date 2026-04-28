# Healthcare RAG Assistant

Healthcare-focused Retrieval-Augmented Generation assistant using local embeddings, ChromaDB, and Groq-hosted Qwen.

# LINK TO WEB-PAGE:- https://health-care-rag-app-dmp2qbrozd6jqytd6wzj9p.streamlit.app/  
## Features

- Upload and index medical PDFs
- Pull abstracts from PubMed directly
- Persistent ChromaDB vector storage
- Qwen 2.5 32B via Groq for grounded answers
- Streamlit chat UI with source citations
- Summarization mode for indexed context

## Project Structure

- `app/config.py` central settings loader
- `app/ingestion` PDF and PubMed ingestion pipeline
- `app/retrieval` vector store and retriever logic
- `app/generation` LLM, prompts, and chain wiring
- `app/ui` sidebar and chat components
- `app/main.py` Streamlit entrypoint
- `tests/` unit tests
- `notebooks/` exploration and evaluation notebooks
- `agent_api/` folder reserved for your API files
# if your are forking it in your system
-`create your own venv using python command `
-`install requirements using `
```powershell
uv pip instal -r requirements.txt
#or
pip instal -r requirements.txt
#if uv is not installed 
```

Fill `GROQ_API_KEY` in `.env`.
For PubMed, set a real `NCBI_EMAIL` in `.env` (NCBI requests this for API usage).
Set `LLM_MODEL` to a model ID that exists on Groq today (see [Groq supported models](https://console.groq.com/docs/models)). The repo default is `llama-3.3-70b-versatile`.
Keep `pyarrow==14.0.2` as specified in `requirements.txt` to avoid a known `sentence-transformers` + `datasets` import issue on Windows.

## Run

```powershell
python -m streamlit run app/main.py
```

## Test

```powershell
python -m pytest tests -v
```
