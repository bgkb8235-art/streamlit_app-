import streamlit as st
st.title("Checking the person eligible for vote or not")
#taking the input 
age=st.number_input("Enter your age ")
if st.button("submit")
  if age >= 18
    st.success("You are Eligible to Vote")
else
    st.sorry("You are not eligible to vote")

