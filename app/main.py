import sys
from pathlib import Path

import streamlit as st

ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from app.ui.chat import render_chat
from app.ui.sidebar import render_sidebar

st.set_page_config(page_title="Healthcare RAG Assistant", page_icon="🏥", layout="wide")
st.title("Healthcare RAG Assistant")

settings = render_sidebar()
render_chat(settings)
