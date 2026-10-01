import streamlit as st

st.title("My first deployed app")
name = st.text_input("Madiha")
if name:
    st.write("Hello, " + name)
