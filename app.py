import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="EduGeni", page_icon="📚")
st.title("📚 EduGeni - AI Tutor")

# Configure API Key from Secrets
try:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
    model = genai.GenerativeModel("gemini-1.5-flash")
except Exception as e:
    st.error(f"API Key Error: {e}")
    st.stop()

# Input
topic = st.text_input("Enter a topic (e.g., What is inheritance in Java?)")

if st.button("Generate Answer"):
    if not topic:
        st.warning("Please enter a topic!")
    else:
        with st.spinner("Generating..."):
            try:
                response = model.generate_content(topic)
                st.success("Answer Generated!")
                st.write(response.text)
            except Exception as e:
                st.error(f"Error: {e}")

st.sidebar.info("Project Summit - EduGeni Ready!")
