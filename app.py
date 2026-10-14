import streamlit as st
import requests

st.set_page_config(page_title="EduGeni", page_icon="📚")
st.title("📚 EduGeni - AI Tutor")

topic = st.text_input("Enter a topic (e.g., What is inheritance in Java?)")

if st.button("Generate Answer"):
    if not topic:
        st.warning("Please enter a topic!")
    else:
        with st.spinner("Generating..."):
            try:
                api_key = st.secrets["GEMINI_API_KEY"]

                url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent"

                headers = {
                    "x-goog-api-key": api_key,
                    "Content-Type": "application/json"
                }

                data = {
                    "contents": [{
                        "parts": [{"text": topic}]
                    }]
                }

                response = requests.post(url, headers=headers, json=data)

                if response.status_code == 200:
                    result = response.json()
                    text = result['candidates'][0]['content']['parts'][0]['text']
                    st.success("Answer Generated!")
                    st.write(text)
                else:
                    st.error(f"Error {response.status_code}: {response.text}")

            except Exception as e:
                st.error(f"Error: {e}")
