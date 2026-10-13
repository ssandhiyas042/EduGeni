import streamlit as st
import requests

st.set_page_config(page_title="EduGeni AI", page_icon="🤖", layout="centered")
st.title("EduGeni - ChatGPT for Students 🤖")
st.write("Enna doubt kettalum ketkalaam da!")

# SIDEBAR LA KEY KEKKA POROM - SECRETS VENAM!
st.sidebar.header("🔑 Setup")
api_key = st.sidebar.text_input("Groq API Key inga paste pannu:", type="password", help="gsk_ nu start aagura key")
st.sidebar.info("Key illaya? groq.com/keys la free ya edukkalam!")

subject = st.sidebar.selectbox("Subject", ["Maths","Science","English","Social Science","Computer Science"])

q = st.text_input(f"Ungal {subject} doubt ah type pannunga:")

def get_answer(question, subject, key):
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {"Authorization": f"Bearer {key}", "Content-Type": "application/json"}
    data = {
        "model": "llama-3.3-70b-versatile",
        "messages": [
            {"role": "system", "content": f"You are EduGeni, friendly Tamil+English {subject} teacher for 10th std. Explain simple, with Tamil touch. Format: Definition, Easy Explanation, Example, Exam Tip."},
            {"role": "user", "content": question}
        ],
        "temperature": 0.7
    }
    r = requests.post(url, headers=headers, json=data, timeout=30)
    if r.status_code == 200:
        return r.json()['choices'][0]['message']['content']
    else:
        return f"Error da: {r.text}"

if st.button("Get Answer ✨"):
    if not api_key:
        st.error("Sidebar la Groq API Key paste pannu da Sandhiya!")
    elif not q:
        st.warning("Question type pannu da!")
    else:
        with st.spinner("ChatGPT maari yosikuthu..."):
            ans = get_answer(q, subject, api_key)
            st.success("Answer:")
            st.markdown(ans)

st.caption("Made with ❤️ by Sandhiya | ChatGPT maari working!")
