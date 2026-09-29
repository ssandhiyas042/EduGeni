import streamlit as st

st.set_page_config(page_title="EduGeni - Your Buddy", page_icon="📚")
st.title("EduGeni - Your Study Buddy 🤖")
st.sidebar.header("Choose Subject")

subject = st.sidebar.selectbox("Select Subject 📚", 
    ["Maths", "Science", "English", "Social Science", "Computer Science"])

question = st.text_input(f"Ask your {subject} doubt:")

if st.button("Get Answer ✨"):
    if not question:
        st.warning("Please enter a question!")
    else:
        st.balloons()
        st.info(f"You asked about {subject}: {question}")
        st.subheader("Here is the answer 💡")
        q = question.lower()

        if subject == "Computer Science":
            if "define" in q and "computer" in q:
                st.write("**Definition of Computer:** A Computer is an electronic device that takes input, processes data, and gives output.")
                st.write("**Characteristics:** Speed, Accuracy, Storage, Automation")
                st.write("**Example:** Laptop takes keyboard input and shows output on screen.")
                st.write("**Formula/Parts:** Input -> Process (CPU) -> Output, IPO Cycle")
            elif "python" in q or "loop" in q:
                st.write("**Definition of Loop:** Loop is used to repeat a block of code.")
                st.write("**Example Code:**")
                st.code("for i in range(5):\n    print(i)")
                st.write("**Explanation:** This prints numbers from 0 to 4.")
                st.write("**Concept:** For loop, While loop")
            else:
                st.write(f"**Definition of {question}:** {question} is an important concept in Computer Science.")
                st.write(f"**Explanation:** It is related to how computer hardware and software work together.")
                st.write(f"**Example:** {question} is used in real-world applications like mobile apps and websites.")
                st.write(f"**Concept:** Understanding {question} with practical code examples.")

        elif subject == "Science":
            if "newton" in q and ("3" in q or "third" in q):
                st.write("**Definition:** Newton's Third Law - Every action has an equal and opposite reaction.")
                st.write("**Formula:** F_action = -F_reaction")
                st.write("**Example:** Rocket launch, jumping from a boat")
                st.write("**Explanation:** When you push a wall, the wall pushes you back.")
            elif "photosynthesis" in q:
                st.write("**Definition:** Photosynthesis is the process by which plants make their food using sunlight.")
                st.write("**Formula:** 6CO2 + 6H2O + Sunlight -> C6H12O6 + 6O2")
                st.write("**Example:** Green leaves making food in sunlight.")
                st.write("**Explanation:** It is essential for all life on earth.")
            else:
                st.write(f"**Definition of {question}:** {question} is an important concept in Science.")
                st.write(f"**Explanation:** {question} explains natural phenomena around us.")
                st.write(f"**Example:** {question} can be observed in daily life activities.")
                st.write(f"**Formula/Diagram:** Draw a diagram for {question} and remember the related formula.")

        elif subject == "Maths":
            if "pythagoras" in q:
                st.write("**Definition:** Pythagoras Theorem - In a right-angled triangle, a² + b² = c²")
                st.write("**Formula:** a² + b² = c²")
                st.write("**Example:** If a=3, b=4, then c=5 because 9+16=25")
                st.write("**Explanation:** It is used to find sides of a right-angled triangle.")
            else:
                st.write(f"**Definition of {question}:** {question} is a mathematical concept used to solve problems.")
                st.write(f"**Formula:** Formula related to {question} should be noted and memorized.")
                st.write(f"**Example:** Solve 2-3 examples of {question} step by step.")
                st.write(f"**Explanation:** Regular practice of {question} helps in scoring full marks.")

        elif subject == "English":
            st.write(f"**Definition of {question}:** {question} is an important concept in English grammar and literature.")
            st.write(f"**Explanation:** Understanding {question} helps in speaking and writing correctly.")
            st.write(f"**Example:** Example - Learning {question} improves communication skills.")
            st.write(f"**Tip:** Write 3 example sentences for {question} and practice reading aloud.")

        else:
            st.write(f"**Definition of {question}:** {question} is an important concept in Social Science.")
            st.write(f"**Explanation:** {question} has played a significant role in history and society.")
            st.write(f"**Example:** Learning {question} helps to understand our country and the world.")
            st.write(f"**Tip:** Remember {question} using Map, Timeline and Story method.")

        st.success("Tip: Write this in your notebook 2 times for better memory! ✨")
