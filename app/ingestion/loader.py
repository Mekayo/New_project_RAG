from pathlib import Path
from typing import Iterable, List

from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader
from langchain_core.documents import Document


def load_documents(data_path: str = "data/raw") -> List[Document]:
    loader = DirectoryLoader(
        data_path,
        glob="**/*.pdf",
        loader_cls=PyPDFLoader,
        show_progress=True,
        use_multithreading=True,
    )
    return loader.load()


def load_uploaded_files(uploaded_files: Iterable, data_path: str = "data/raw") -> List[Document]:
    target_dir = Path(data_path)
    target_dir.mkdir(parents=True, exist_ok=True)
    for file in uploaded_files:
        file_path = target_dir / file.name
        file_path.write_bytes(file.getbuffer())
    return load_documents(str(target_dir))
