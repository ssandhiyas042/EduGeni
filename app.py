import streamlit as st
from openai import OpenAI

# --- Page Config ---
st.set_page_config(page_title="EduGenie - Study Buddy", page_icon="🎓", layout="centered")

st.title("🎓 EduGenie - Study Buddy")
st.caption("Your AI-powered study assistant")

# --- Inputs ---
col1, col2 = st.columns(2)
with col1:
    subject = st.selectbox("Select Subject", ["Java", "Python", "Data Structure", "English"])

with col2:
    language = st.selectbox("Select Language", ["Tamil", "English"])

answer_type = st.selectbox("Answer Format", ["Simple Explanation", "2-Mark", "5-Mark", "10-Mark"])

question = st.text_area("Enter your question here", placeholder="Ex: What is inheritance in Java?")

# --- Session State for Loop Fix ---
if "final_answer" not in st.session_state:
    st.session_state.final_answer = ""

# --- Core Function with Correct Prompt ---
def generate_answer(question, subject, language, answer_type):
    client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

    system_instruction = """
    You are an expert teacher for college students.
    You must give accurate, correct, and specific answers.
    NEVER repeat the user's question as the definition.
    ALWAYS give real definition, syntax, example code if subject is Java/Python/Data Structure.
    Do not give generic tips like 'write 2 times' or 'very important for exams'.
    If user spelling is wrong, auto-correct and answer correctly.
    """

    user_prompt = f"""
    Subject: {subject}
    Language: {language}
    Required Answer Format: {answer_type}
    Student Question: {question}

    Instructions:
    - Answer in {language} language only.
    - If subject is Java/Python/Data Structure, provide definition, syntax, and example program.
    - If subject is English, provide grammar, definition and examples.
    - Keep answer according to {answer_type} format.
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        temperature=0.2,
        messages=[
            {"role": "system", "content": system_instruction},
            {"role": "user", "content": user_prompt}
        ]
    )
    return response.choices[0].message.content

# --- Generate Button Logic ---
if st.button("Generate Answer", use_container_width=True, type="primary"):
    if not question.strip():
        st.warning("Please enter a question first!")
    else:
        with st.spinner("Generating correct answer..."):
            try:
                st.session_state.final_answer = generate_answer(question, subject, language, answer_type)
            except Exception as e:
                st.error(f"Error occurred: {e}")

# --- Display Answer ---
if st.session_state.final_answer:
    st.divider()
    st.subheader("Answer:")
    st.markdown(st.session_state.final_answer)
    st.divider()
    if st.button("Clear Answer"):
        st.session_state.final_answer = ""
        st.rerun()
