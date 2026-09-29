import streamlit as st

st.set_page_config(page_title="EduGeni - Teacher Mode", page_icon="👩‍🏫")
st.title("EduGeni - Your Teacher 👩‍🏫")
st.write("Hello Students! Ask any doubt, I will explain like your class teacher!")

subject = st.sidebar.selectbox("Select Subject 📚", 
    ["Maths", "Science", "English", "Social Science", "Computer Science"])

question = st.text_input(f"Enter your {subject} question:")

def teacher_answer(topic, subject):
    st.markdown(f"### Okay class, today we will learn about {topic} in {subject}!")
    
    if subject == "Computer Science":
        if "python" in topic.lower():
            st.write("**1. Definition:** Python is a high-level programming language. It is very easy to read and write.")
            st.write("**2. Teacher Explanation:** See children, imagine Python is like English language for computers. Just like you talk to your friend in English, we talk to computer in Python. It was invented by Guido van Rossum.")
            st.write("**3. Real Life Example:** YouTube, Instagram, Google - all these apps are built using Python.")
            st.write("**4. Code Example:**")
            st.code('print("Hello Students!")\n# This will print Hello Students on screen')
            st.write("**5. Why Important:** If you learn Python, you can make games, websites and even AI like me!")
        elif "loop" in topic.lower():
            st.write("**1. Definition:** Loop means doing same work again and again.")
            st.write("**2. Teacher Explanation:** Children, imagine you have to write 'I will do homework' 10 times. Instead of writing 10 times, loop will do it for you automatically!")
            st.write("**3. Real Life Example:** Clock ticking every second is a loop. Fan rotating again and again is a loop.")
            st.write("**4. Code Example:**")
            st.code("for i in range(1, 6):\n    print(f'Number {i}')\n# Prints 1 to 5")
            st.write("**5. Types:** For Loop - when you know how many times, While Loop - when you don't know")
        elif "computer" in topic.lower():
            st.write("**1. Definition:** Computer is an electronic machine that takes input, processes it and gives output.")
            st.write("**2. Teacher Explanation:** See, when you type A on keyboard (input), CPU thinks (process), and A appears on screen (output). That is computer!")
            st.write("**3. Real Life Example:** Your mobile phone is also a small computer.")
            st.write("**4. Diagram:** Input (Keyboard) -> Process (CPU) -> Output (Screen) [IPO Cycle]")
            st.write("**5. Why Important:** Without computer, no WhatsApp, no games, no online class!")
        else:
            st.write(f"**1. Definition:** {topic} is a very important topic in {subject}.")
            st.write(f"**2. Teacher Explanation:** Children, {topic} is like a building block. If you understand {topic}, you can easily understand next chapters in {subject}. Let me explain in simple words.")
            st.write(f"**3. Real Life Example:** We use {topic} in our daily life. For example, when you use computer or mobile, {topic} is working behind it.")
            st.write(f"**4. Code/Formula:** For {topic}, always remember to practice with small examples.")
            st.write(f"**5. Why Important:** Exam la {topic} la irunthu 5 marks question confirm varum!")

    elif subject == "Science":
        st.write(f"**1. Definition:** {topic} is a natural phenomenon in Science.")
        st.write(f"**2. Teacher Explanation:** Okay children, close your eyes and imagine. {topic} is happening all around us. Science is nothing but understanding nature.")
        st.write(f"**3. Real Life Example:** Example for {topic} - Look at your kitchen, your cycle, your garden. You can see {topic} there.")
        st.write(f"**4. Formula/Diagram:** My dear students, for {topic}, draw a neat diagram in exam. Teacher will give full marks!")
        st.write(f"**5. Why Important:** {topic} helps us to understand how this world works. Very important for future scientists!")

    elif subject == "Maths":
        st.write(f"**1. Definition:** {topic} is a mathematical concept that helps us solve problems.")
        st.write(f"**2. Teacher Explanation:** See children, Maths is not difficult. {topic} is like a puzzle game. If you know the formula, you can solve any sum in 2 minutes.")
        st.write(f"**3. Real Life Example:** We use {topic} when we go shopping, when we calculate marks, when we share chocolates!")
        st.write(f"**4. Formula:** Formula for {topic} is very important. Write it 5 times and memorize.")
        st.write(f"**5. Why Important:** 10 marks question will come from {topic} in final exam. So practice well!")

    elif subject == "English":
        st.write(f"**1. Definition:** {topic} is a concept in English grammar/literature.")
        st.write(f"**2. Teacher Explanation:** Children, English is a global language. If you learn {topic}, you can speak confidently like me!")
        st.write(f"**3. Real Life Example:** Example sentence: 'My teacher explained {topic} very clearly today.'")
        st.write(f"**4. Tip:** For {topic}, read 3 examples and write 3 sentences daily.")
        st.write(f"**5. Why Important:** Good English means good job in future!")

    else: # Social
        st.write(f"**1. Definition:** {topic} is an important event/concept in Social Science.")
        st.write(f"**2. Teacher Explanation:** Dear students, history is not just dates. {topic} tells us a story about our ancestors and how our country was formed.")
        st.write(f"**3. Real Life Example:** We can still see the effect of {topic} in our society today.")
        st.write(f"**4. Map/Timeline:** For {topic}, always mark on map and write years. That is the secret to get full marks!")
        st.write(f"**5. Why Important:** {topic} teaches us values and helps us become good citizens!")

if st.button("Explain Like My Teacher 👩‍🏫"):
    if not question:
        st.warning("Dear student, please ask a question first!")
    else:
        st.balloons()
        teacher_answer(question, subject)
        st.success("Did you understand? If not, ask again! Your teacher is here! ✨")
