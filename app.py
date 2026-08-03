import streamlit as st

st.title("Checking the person eligible for vote or not")

# Taking the input
age = st.number_input("Enter your age", min_value=0)

if st.button("Submit"):
    if age >= 18:
        st.success("You are eligible to vote.")
    else:
        st.error("You are not eligible to vote.")
