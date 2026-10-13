import streamlit as st
import requests

st.set_page_config(page_title="EduGeni for Students", page_icon="📚", layout="centered")
st.title("EduGeni - For Students 👩‍🎓")
st.write("Hello Students! I am your teacher. Ask any doubt from 5 subjects, I will explain clearly!")

subject = st.sidebar.selectbox("Choose Your Subject 📚",
    ["Maths", "Science", "English", "Social Science", "Computer Science"])

st.sidebar.info(f"Subject: {subject}\n\nAsk any question, you will get Definition!")

question = st.text_input(f"Ask your {subject} doubt here:")

# Function to get real definition from Wikipedia
def get_wiki_def(topic):
    try:
        url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{topic.replace(' ', '_')}"
        headers = {"User-Agent": "EduGeniApp/1.0"}
        r = requests.get(url, headers=headers, timeout=5)
        data = r.json()
        if "extract" in data and data["extract"]:
            return data["extract"]
    except:
        return None
    return None

# Local strong knowledge for important topics
local_db = {
    "types of noun": "**Noun - 5 Types:** 1) Proper Noun (specific name - Ram, Delhi) 2) Common Noun (general - boy, city) 3) Collective Noun (group - team, family) 4) Abstract Noun (feeling - honesty, love) 5) Material Noun (material - gold, water). Example: Ram is a boy with honesty.",
    "noun": "**Noun:** Naming word. Name of person, place, animal, thing. Types: Proper, Common, Collective, Abstract, Material.",
    "verb": "**Verb:** Action word. Eg: eat, sleep, run, write. Types: Main verb, Helping verb (is, am, are, was, were).",
    "tense": "**Tense:** Tells time of action. 3 types: Present (I eat), Past (I ate), Future (I will eat). Each has Simple, Continuous, Perfect, Perfect Continuous.",
    "photosynthesis": "**Photosynthesis:** Process where green plants make food using Sunlight, CO2, Water. Formula: CO2 + Water + Sunlight -> Glucose + Oxygen. Happens in chloroplast of leaf.",
    "python": "**Python:** High-level easy programming language invented by Guido van Rossum. Used in YouTube, Instagram, AI. Code: print('Hello')",
}

if st.button("Get Answer From Teacher 👩‍🏫"):
    if not question:
        st.warning("Please enter a question!")
    else:
        st.balloons()
        q_low = question.lower().strip()
        st.subheader(f"Okay class, let's learn {question} in {subject}!")

        answer_found = None

        # 1. Check local db first
        for key in local_db:
            if key in q_low or q_low in key:
                answer_found = local_db[key]
                break

        # 2. If not in local, get from Wikipedia
        if not answer_found:
            wiki = get_wiki_def(question)
            if wiki:
                answer_found = wiki
            else:
                answer_found = f"{question} is a very important concept in {subject}. It is widely used and very important for exams."

        st.write(f"**1. Definition:** {answer_found}")

        # Teacher style explanation for all 5 subjects
        if subject == "Computer Science":
            st.write(f"**2. Explanation:** Children, {question} helps computer to work smarter. It is like brain for computer.")
            st.write(f"**3. Example Code:** Try small program for {question} and run it.")
        elif subject == "Science":
            st.write(f"**2. Explanation:** {question} is happening around us in nature. Science helps us understand it.")
            st.write(f"**3. Example:** You can see {question} in your kitchen, garden, lab.")
            st.write(f"**4. Diagram:** Draw neat diagram for {question} for full marks.")
        elif subject == "Maths":
            st.write(f"**2. Explanation:** {question} is like a puzzle. If you know formula, you can solve any sum in 2 mins.")
            st.write(f"**3. Formula:** Note formula for {question} and practice 3 sums daily.")
        elif subject == "English":
            st.write(f"**2. Explanation:** If you learn {question}, you can speak English confidently.")
            st.write(f"**3. Example:** Make 2 sentences daily using {question}.")
        else:
            st.write(f"**2. Explanation:** {question} tells story of our country and society. Important for becoming good citizen.")
            st.write(f"**3. Example:** Effect of {question} can be seen in our village today.")

        st.write(f"**4. Why Important:** {question} is a 5 marks question in exam. Prepare well!")
        st.write(f"**5. Exam Tip:** Write heading '{question}' neatly, add points and example - Full marks!")

        st.success("Understood? Write this 2 times in notebook! You will get full marks! ✨")
