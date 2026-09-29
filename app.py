import streamlit as st

st.set_page_config(page_title="EduGeni - Your Buddy", page_icon="📚")
st.title("EduGeni - Your Study Buddy 🤖")
st.sidebar.header("Choose Subject")

subject = st.sidebar.selectbox("Select Subject 📚", 
    ["Maths", "Science", "English", "Social Science", "Computer Science"])

st.sidebar.success(f"You selected {subject}!")

question = st.text_input(f"Ask your {subject} doubt:")

if st.button("Get Answer ✨"):
    if question:
        st.balloons()
        st.info(f"You asked about {subject}: {question}")
        q = question.lower()

        if subject == "Maths":
            if "pythagoras" in q:
                st.subheader("Here is the answer 💡")
                st.write("**Pythagoras Theorem:** a² + b² = c²")
                st.write("Example: a=3, b=4 => c=5")
            else:
                st.write(f"**Answer for {question}:** Practice with examples da!")

        elif subject == "Science":
            if "newton" in q and "3" in q:
                st.subheader("Here is the answer 💡")
                st.write("**Newton's 3rd Law:** Every action has equal opposite reaction.")
                st.write("Example: Rocket launch, Boat jump")
                st.write("Formula: F_action = -F_reaction")
            elif "newton" in q:
                st.write("**Newton's Laws:** 1st - rest/motion, 2nd - F=ma, 3rd - action-reaction")
            elif "photosynthesis" in q:
                st.write("**Photosynthesis:** 6CO2+6H2O+Sunlight -> Food + O2")
            else:
                st.write(f"**Answer for {question}:** Science example from daily life da!")

        elif subject == "English":
            st.write(f"**Answer for {question}:** Story maathiri padicha easy da!")

        elif subject == "Social Science":
            st.write(f"**Answer for {question}:** Map + Timeline vechu padicha 100% mark!")

        else:
            if "python" in q:
                st.write("**Python Loop:** for i in range(5): print(i)")
            else:
                st.write(f"**Answer for {question}:** Code + example paathu purinjikka laam!")

        st.success("Tip: Write in notebook 2 times!✨")
    else:
        st.warning("Please type a question!")
