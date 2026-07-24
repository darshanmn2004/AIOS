import streamlit as st
from llm.ollama_client import generate_response

def render_chat():

    st.title("🤖 AIOS")

    st.caption("Autonomous Personal AI Assistant")

    st.markdown("---")

    # Display previous messages
    for message in st.session_state.messages:

        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Chat input
    prompt = st.chat_input("Type your message...")

    if prompt:

        # Store user message
        st.session_state.messages.append(
            {
                "role": "user",
                "content": prompt
            }
        )

        with st.chat_message("user"):
            st.markdown(prompt)

        # Placeholder response
        with st.spinner("Thinking..."):
          response = generate_response(prompt)

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": response
            }
        )

        with st.chat_message("assistant"):
            st.markdown(response)