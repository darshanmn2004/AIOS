import streamlit as st


def render_sidebar():
    with st.sidebar:

        st.title("🤖 AIOS")

        st.markdown("---")

        if st.button("🆕 New Chat", use_container_width=True):

            st.session_state.messages = [
                {
                    "role": "assistant",
                    "content": "👋 Hello! I'm AIOS.\n\nHow can I help you today?"
                }
            ]

            st.rerun()

        st.markdown("---")

        st.subheader("Settings")

        st.info("Coming Soon")

        st.markdown("---")

        st.caption("Version 0.1.0")