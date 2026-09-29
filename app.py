import streamlit as st

st.set_page_config(page_title="EduGeni - Your Buddy", page_icon="📚")
st.title("EduGeni - Your Study Buddy 🤖")
st.sidebar.header("Choose Subject")

subject = st.sidebar.selectbox("Select Subject 📚", 
    ["Maths", "Science", "English", "Social Science", "Computer Science"])

question = st.text_input(f"Ask your {subject} doubt:")
q = question.lower() if question else ""

if st.button("Get Answer ✨"):
    if not question:
        st.warning("Please type a question!")
    else:
        st.balloons()
        st.info(f"You asked about {subject}: {question}")
        st.subheader("Here is the answer 💡")

        if subject == "Computer Science":
            if "computer" in q and "define" in q:
                st.write("**Definition of Computer:**")
                st.write("A Computer is an electronic device that takes input, processes data, and gives output.")
                st.write("**Characteristics:** Speed, Accuracy, Storage, Automation")
                st.write("**Example:** Your laptop takes keyboard input and shows output on screen.")
                st.write("**Formula/Parts:** Input -> Process (CPU) -> Output, IPO cycle")
            elif "python" in q or "loop" in q:
                st.write("**Python Loop:** Used to repeat code.")
                st.code("for i in range(5):\n    print(i)  # 0,1,2,3,4")
            elif "ai" in q:
                st.write("**AI (Artificial Intelligence):** Making computers think like humans. Eg: ChatGPT, EduGeni")
            else:
                st.write(f"**{question}:** In Computer Science, this means understanding how hardware and software work together with a real example.")

        elif subject == "Science":
            if "newton" in q:
                if "3" in q or "third" in q:
                    st.write("**Newton's 3rd Law:** Every action has equal and opposite reaction.")
                    st.write("Example: Rocket pushes gas down, gas pushes rocket up. F_action = -F_reaction")
                elif "1" in q: st.write("**1st Law:** Object stays at rest/motion unless force acts. Eg: Book on table.")
                elif "2" in q: st.write("**2nd Law:** F = m x a. Eg: 5kg box with 10N => 2 m/s²")
                else: st.write("**Newton's 3 Laws:** 1) Inertia, 2) F=ma, 3) Action-Reaction")
            elif "photosynthesis" in q:
                st.write("**Photosynthesis:** Plants make food using sunlight.")
                st.write("Equation: 6CO2 + 6H2O + Sunlight -> C6H12O6 + 6O2")
            else:
                st.write(f"**{question}:** This is a Science concept. Learn it with a daily life example - like kitchen, cycle, plants!")

        elif subject == "Maths":
            if "pythagoras" in q: st.write("**Pythagoras:** a²+b²=c². Eg: 3²+4²=5²")
            elif "algebra" in q: st.write("**Algebra:** Finding unknown. x+2=5 => x=3")
            else: st.write(f"**{question}:** Solve with 2-3 examples step by step da!")

        elif subject == "English":
            if "tenses" in q: st.write("**Tenses:** Present - I eat, Past - I ate, Future - I will eat")
            else: st.write(f"**{question}:** Learn this with story and example sentences!")

        else: # Social
            if "revolution" in q: st.write("**French Revolution 1789:** Liberty, Equality, Fraternity")
            else: st.write(f"**{question}:** Remember with Map + Year + Story!")

        st.success("Tip: Write this in notebook 2 times! ✨")
