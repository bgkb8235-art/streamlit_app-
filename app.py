import streamlit as st

st.title("Checking the person eligible for vote or not")

age = st.number_input(
    "Enter your age",
    min_value=0,
    max_value=100,
    step=1
)

if st.button("Submit"):
    if age >= 18:
        st.success("You are eligible to vote.")
    else:
        st.error("You are not eligible to vote.")
