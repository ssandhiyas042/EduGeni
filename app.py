import streamlit as st
import requests

st.set_page_config(page_title="EduGeni AI", layout="centered")
st.title("EduGeni AI")
st.write("Ask any doubt - ChatGPT style answers")

# Input for API Key
api_key = st.text_input("Enter Groq API Key:", type="password", placeholder="gsk_...")

# Subject selection
subject = st.selectbox("Choose Subject", ["General", "Maths", "Science", "English", "Social", "Computer Science"])

# Initialize chat history
if "history" not in st.session_state:
    st.session_state.history = []

# Display history
for chat in st.session_state.history:
    with st.chat_message(chat["role"]):
        st.write(chat["content"])

# Chat input
if question := st.chat_input(f"Ask {subject} question..."):
    if not api_key:
        st.error("Enter API Key first!")
    else:
        # User message
        st.session_state.history.append({"role": "user", "content": question})
        with st.chat_message("user"):
            st.write(question)

        # AI response
        with st.chat_message("assistant"):
            with st.spinner("Generating answer..."):
                try:
                    url = "https://api.groq.com/openai/v1/chat/completions"
                    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
                    payload = {
                        "model": "llama-3.3-70b-versatile",
                        "messages": [
                            {"role": "system", "content": f"You are a helpful {subject} teacher. Explain clearly in simple English for Class 10 students. Give definition, explanation, example and exam tip."},
                            {"role": "user", "content": question}
                        ]
                    }
                    response = requests.post(url, headers=headers, json=payload, timeout=30)
                    result = response.json()
                    answer = result["choices"][0]["message"]["content"]

                    st.write(answer)
                    st.session_state.history.append({"role": "assistant", "content": answer})
                except Exception as e:
                    st.error(f"Error: {e}")
