import streamlit as st

st.set_page_config(page_title="EduGeni - Study Buddy", page_icon="🎓")
st.title("EduGeni - Your Study Buddy 🎓")

# Step 1: Who are you?
role = st.sidebar.radio("Login as:", ["Student 👩‍🎓", "Teacher 👩‍🏫"])
subject = st.sidebar.selectbox("Subject 📚", ["Maths", "Science", "English", "Social Science", "Computer Science"])
st.sidebar.success(f"Logged in as {role}")

if "db" not in st.session_state:
    st.session_state.db = {}

# STUDENT LOGIN
if role == "Student 👩‍🎓":
    st.header(f"Hello Student! Ask your {subject} doubt 👩‍🎓")
    q = st.text_input("Type your question here:")
    
    if st.button("Get Answer ✨"):
        if not q:
            st.warning("Please type a question!")
        else:
            st.balloons()
            low_q = q.lower()
            
            # Check if teacher added answer
            if low_q in st.session_state.db:
                st.subheader(f"Answer for {q}:")
                st.write(st.session_state.db[low_q])
            else:
                st.subheader(f"Teacher explains {q}:")
                
                if subject == "Computer Science":
                    if "python" in low_q:
                        st.write("**Definition:** Python is a high-level, easy programming language.")
                        st.write("**Explanation:** We use Python to talk to computers. It is like English for computers. Made by Guido van Rossum.")
                        st.write("**Example:**")
                        st.code('print("Hello World")')
                        st.write("**Use:** YouTube, Instagram, AI are made with Python.")
                    elif "loop" in low_q:
                        st.write("**Definition:** Loop is used to repeat same work again and again.")
                        st.write("**Explanation:** If you want to print 1 to 100, you don't type 100 times. Loop will do it!")
                        st.write("**Example:**")
                        st.code("for i in range(5):\n    print(i)")
                    elif "computer" in low_q:
                        st.write("**Definition:** Computer is an electronic device that takes Input, Processes and gives Output.")
                        st.write("**Explanation:** Keyboard -> CPU -> Monitor is called IPO cycle.")
                        st.write("**Example:** Laptop, Mobile are computers.")
                    else:
                        st.write(f"**Definition:** {q} is an important concept in Computer Science.")
                        st.write(f"**Explanation:** {q} helps computer to work faster and smarter.")
                        st.write(f"**Example:** {q} is used in apps like WhatsApp and Google.")
                elif subject == "Science":
                    st.write(f"**Definition:** {q} is an important topic in Science.")
                    st.write(f"**Explanation:** {q} is happening around us in nature. Science explains it.")
                    st.write(f"**Example:** We can see {q} in our daily life - kitchen, garden, road.")
                    st.write(f"**Formula:** Draw diagram for {q} and remember formula.")
                elif subject == "Maths":
                    st.write(f"**Definition:** {q} is a Maths concept to solve problems.")
                    st.write(f"**Explanation:** Maths is a game. If you know formula of {q}, you can solve any sum in 2 minutes.")
                    st.write(f"**Formula:** Note formula for {q} and practice 3 sums.")
                    st.write(f"**Example:** We use {q} in shopping and marks calculation.")
                elif subject == "English":
                    st.write(f"**Definition:** {q} is a concept in English.")
                    st.write(f"**Explanation:** Learning {q} helps you speak and write good English.")
                    st.write(f"**Example:** Eg: 'I learned {q} today from my teacher.'")
                else:
                    st.write(f"**Definition:** {q} is an important concept in Social Science.")
                    st.write(f"**Explanation:** {q} tells us story about our country and history.")
                    st.write(f"**Example:** We learn {q} to understand our society.")
                
                st.success("Write this 2 times in your notebook! ✨")

# TEACHER LOGIN
else:
    st.header("Hello Teacher! Add new lesson here 👩‍🏫")
    topic = st.text_input("Enter Topic Name (eg: python):")
    ans = st.text_area("Enter Full Answer (Definition + Explanation + Example):")
    
    if st.button("Add Lesson ➕"):
        if topic and ans:
            st.session_state.db[topic.lower()] = ans
            st.success(f"Added {topic}! Students can see it now!")
        else:
            st.warning("Enter both topic and answer!")
            
    st.write("### Added Lessons:")
    st.write(st.session_state.db)
