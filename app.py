import streamlit as st

st.set_page_config(page_title="EduGeni for Students", page_icon="📚")
st.title("EduGeni - For Students 👩‍🎓")
st.write("Hello Students! I am your teacher. Ask any doubt, I will explain clearly!")

subject = st.sidebar.selectbox("Choose Your Subject 📚",
    ["Maths", "Science", "English", "Social Science", "Computer Science"])

question = st.text_input(f"Ask your {subject} doubt here:")

if st.button("Get Answer From Teacher 👩‍🏫"):
    if not question:
        st.warning("Please enter your question dear student!")
    else:
        st.balloons()
        q = question.lower()
        st.subheader(f"Okay class, let's learn {question} in {subject}!")

        if subject == "Computer Science":
            if "python" in q:
                st.write("**1. Definition:** Python is a high-level programming language, easy to learn.")
                st.write("**2. Explanation:** Children, Python is like English for computers. We use it to tell computer what to do. It was created by Guido van Rossum.")
                st.write("**3. Example:**")
                st.code('print("Hello Students")\nname = "Sandhiya"\nprint(name)')
                st.write("**4. Where it is used:** YouTube, Instagram, Google and even AI like me are made with Python.")
                st.write("**5. Exam Tip:** Write this code 2 times, you will get full marks!")
            
            elif "loop" in q:
                st.write("**1. Definition:** Loop means repeating same work again and again.")
                st.write("**2. Explanation:** Imagine you have to write your name 10 times. Loop will do it in 1 line, instead of 10 lines!")
                st.write("**3. Example:**")
                st.code("for i in range(5):\n    print('I will study daily')")
                st.write("**4. Types:** For Loop (when you know count), While Loop (when you don't know count)")
                st.write("**5. Exam Tip:** Draw flowchart for loop in exam!")
            
            elif "computer" in q:
                st.write("**1. Definition:** Computer is an electronic device that takes Input, Processes data and gives Output.")
                st.write("**2. Explanation:** See children, when you press A on keyboard (Input), CPU thinks (Process), A comes on screen (Output). This is IPO cycle.")
                st.write("**3. Example:** Laptop, Mobile phone are computers.")
                st.write("**4. Parts:** Input Unit, CPU, Memory, Output Unit")
                st.write("**5. Exam Tip:** Draw IPO diagram for 2 marks!")
            
            else:
                st.write(f"**1. Definition:** {question} is an important concept in Computer Science.")
                st.write(f"**2. Explanation:** Children, {question} helps computer to do work faster. It is like brain for computer.")
                st.write(f"**3. Example:** {question} is used in real apps like WhatsApp, Google, Games.")
                st.write(f"**4. How to Learn:** Write small code for {question} and run it.")
                st.write(f"**5. Exam Tip:** This is 5 marks question, practice well!")

        elif subject == "Science":
            st.write(f"**1. Definition:** {question} is an important topic in Science.")
            st.write(f"**2. Explanation:** Okay students, Science means understanding nature. {question} is happening all around us daily.")
            st.write(f"**3. Example:** Example - You can see {question} in your kitchen, garden and school lab.")
            st.write(f"**4. Formula / Diagram:** For {question}, always draw a neat diagram with labels. Teacher will give full marks!")
            st.write(f"**5. Why Important:** If you understand {question}, you can become a great scientist!")

        elif subject == "Maths":
            st.write(f"**1. Definition:** {question} is a mathematical concept to solve problems.")
            st.write(f"**2. Explanation:** See, Maths is not tough. {question} is like a puzzle. If you know the formula, you can solve any sum in 2 minutes.")
            st.write(f"**3. Example:** Example - We use {question} in shopping, cricket score and marks calculation.")
            st.write(f"**4. Formula:** Formula for {question} - Write it 5 times and memorize it!")
            st.write(f"**5. Exam Tip:** 10 marks question will come from {question}. Practice 3 sums daily!")

        elif subject == "English":
            st.write(f"**1. Definition:** {question} is a concept in English Grammar.")
            st.write(f"**2. Explanation:** Children, if you learn {question}, you can speak English confidently like your teacher.")
            st.write(f"**3. Example:** Sentence - 'My teacher taught me {question} very clearly today.'")
            st.write(f"**4. How to Practice:** Write 3 sentences using {question} daily and read aloud.")
            st.write(f"**5. Exam Tip:** Good English = Good Job in future!")

        else: # Social Science
            st.write(f"**1. Definition:** {question} is an important concept in Social Science.")
            st.write(f"**2. Explanation:** Dear students, {question} is not just a lesson, it is a story of our country and our ancestors.")
            st.write(f"**3. Example:** We can see the effect of {question} in our village and society today.")
            st.write(f"**4. How to Remember:** For {question}, use Map + Year + Story method. Easy to remember!")
            st.write(f"**5. Exam Tip:** Write point wise with dates for full marks!")

        st.success("Understood? Write this in your notebook 2 times! You will get full marks! ✨")
