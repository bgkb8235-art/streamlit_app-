import streamlit as st

# Title
st.title("Checking the person eligible for vote or not")

# Taking the input
age = st.number_input("Enter your age", min_value=0, step=1)

# Button
if st.button("Submit"):
    if age > 100:
        st.error("Invalid age input!")
    elif age >= 18:
        st.success("You are eligible to vote.")
    else:
        st.error("You are not eligible to vote.")
