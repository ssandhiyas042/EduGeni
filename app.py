import streamlit as st
from google import genai

st.set_page_config(page_title="EduGeni", page_icon="📚")
st.title("📚 EduGeni - AI Tutor")

try:
    client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])
except Exception as e:
    st.error(f"API Key Error: {e}")
    st.stop()

topic = st.text_input("Enter a topic")

if st.button("Generate Answer"):
    if not topic:
        st.warning("Please enter a topic!")
    else:
        with st.spinner("Generating..."):
            try:
                response = client.models.generate_content(
                    model="gemini-2.0-flash",
                    contents=topic
                )
                st.success("Answer Generated!")
                st.write(response.text)
            except Exception as e:
                st.error(f"Error: {e}")
