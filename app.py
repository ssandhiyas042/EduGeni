import streamlit as st

st.set_page_config(page_title="EduGenie", page_icon="🧞‍♂️")
st.title("EduGenie - Your Personal Study Buddy 🧞‍♂️")

subject = st.sidebar.selectbox("Select Subject:", ["Maths", "Science"])
st.sidebar.success(f"You selected {subject}!")

question = st.text_input(f"Ask your {subject} doubt:")

if st.button("Get Answer ✨"):

    
    if question:
        st.balloons()
        st.info(f"You asked about {subject}: {question}")
        
        if subject == "Maths":
            if "pythagoras" in question.lower():
                st.subheader("Here is the answer 👇")
                st.write("**Pythagoras Theorem:**")
                st.write("In a right-angled triangle, the square of the hypotenuse is equal to the sum of the squares of the other two sides.")
                st.write("Formula: a² + b² = c²")
                st.write("Example: If a=3, b=4, then c=5 because 3² + 4² = 9+16 = 25 = 5²")
            else:
                st.write(f"**Answer for {question}:**")
                st.write("This is an important topic! If you learn it like a story, you will remember it easily.")
        else:
            st.write(f"**Answer for {question}:**")
            st.write("This is Science! Let's understand with a simple example from daily life.")
            
        st.success("Tip: Write this in your notebook and read it 2 times!")
    else:
        st.warning("Please type a question first!")

st.markdown("---")
st.caption("Made with ❤️ for studies")