import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="EduGeni", page_icon="🎓")
st.title("🎓 EduGeni - Answer Generator")

try:
    api_key = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=api_key)
except Exception as e:
    st.error(f"Secrets la GEMINI_API_KEY illa da! Error: {e}")
    st.stop()

subject = st.selectbox("Subject", ["Java", "Python", "Data Structure", "C", "Other"])
answer_format = st.selectbox("Answer Format", ["Simple Explanation", "Detailed", "Tamil", "Tanglish"])
question = st.text_area("Enter your question here", placeholder="What is inheritance in java")

if st.button("Generate Answer", type="primary"):
    if not question.strip():
        st.warning("Question type pannu da!")
    else:
        with st.spinner("Generating..."):
            try:
                model = genai.GenerativeModel('gemini-1.5-flash')
                prompt = f"Subject: {subject}, Format: {answer_format}, Question: {question}. Give student friendly answer."
                res = model.generate_content(prompt)
                st.success("Answer Ready!")
                st.write(res.text)
            except Exception as e:
                st.error(f"Error: {e}")
