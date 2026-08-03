import streamlit as st

st.title("My first streamlit app")

# Take the text input
name = st.text_input("Enter your name")

if st.button("Submit"):
    st.write(f"Hello, {name}")
