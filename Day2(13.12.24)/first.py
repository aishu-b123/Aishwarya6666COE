import streamlit as st
st.title("Welcome to stream lit")
st.header("even odd program")
num=st.number_input("Enter a number:",step=1)

if st.button("even/odd"):
    if num%2==0:
        st.success("Even number")
    else:
        st.error("Odd number")