import streamlit as st

from ui.sidebar import render_sidebar
from ui.chat import render_chat

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="AIOS",
    page_icon="🤖",
    layout="wide",
)

# -----------------------------
# Session State
# -----------------------------
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "👋 Hello! I'm AIOS.\n\nYour Autonomous Personal AI Assistant.\n\nHow can I help you today?"
        }
    ]

# -----------------------------
# Sidebar
# -----------------------------
render_sidebar()

# -----------------------------
# Main Chat UI
# -----------------------------
render_chat()