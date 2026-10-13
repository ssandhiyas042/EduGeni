import streamlit as st
from openai import OpenAI

st.set_page_config(
    page_title="EduGenie",
    page_icon="🎓",
    layout="centered"
)

st.title("🎓 EduGenie")
st.subheader("Your AI Study Assistant")

st.write("Ask any question. Learn in English, Tamil, or Tanglish!")

with st.sidebar:
    st.header("⚙️ Study Settings")

    language = st.selectbox(
        "Choose language",
        ["Simple English", "Tamil", "Tanglish"]
    )

    answer_type = st.selectbox(
        "Answer type",
        [
            "Simple Explanation",
            "2-Mark Answer",
            "5-Mark Answer",
            "10-Mark Answer",
            "Step-by-Step Solution",
            "Program with Explanation",
            "Quiz"
        ]
    )

    subject = st.selectbox(
        "Choose subject",
        [
            "All Subjects",
            "Computer Science",
            "Python",
            "Java",
            "Mathematics",
            "Science",
            "English",
            "Tamil",
            "Machine Learning",
            "Software Engineering"
        ]
    )

st.markdown("---")

question = st.text_area(
    "📚 Enter your question",
    placeholder="Example: Explain recursion in Python...",
    height=130
)

if st.button("✨ Generate Answer", use_container_width=True):
    if not question.strip():
        st.warning("Please enter your question.")
    else:
        try:
            client = OpenAI(
                api_key=st.secrets["OPENAI_API_KEY"]
            )

            prompt = f"""
            You are EduGenie, an AI study assistant.

            Subject: {subject}
            Language: {language}
            Answer type: {answer_type}

            Explain clearly for a student.
            Use simple language and headings.
            For maths, show steps.
            For programming, provide correct code and explain it.
            For exam answers, follow the requested mark length.
            If Tamil or Tanglish is selected, answer accordingly.

            Student question: {question}
            """

            with st.spinner("EduGenie is preparing your answer..."):
                response = client.responses.create(
                    model="gpt-4.1-mini",
                    input=prompt
                )

            st.markdown("### 📖 Your Answer")
            st.markdown(response.output_text)

        except KeyError:
            st.error(
                "API key missing. Add OPENAI_API_KEY to "
                "Streamlit Secrets before running the app."
            )
        except Exception as e:
            st.error(f"Something went wrong: {e}")

st.markdown("---")
st.caption("EduGenie 🎓 | Learn • Practice • Grow")
