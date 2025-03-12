import streamlit as st
import pandas

st.set_page_config(layout="wide")

st.header("The Best Company")
st.write("""
        Hi, I'm Glaudiston! I'm a skilled JavaScript developer who has recently expanded my expertise in Python.
        My GitHub projects, such as To-do_Web-app and PythonTodoList, showcase my proficiency in building practical
        applications. I graduated in 2019 and have gained valuable experience as a freelancer. Now, I'm eager to
        leverage my knowledge and skills in a dynamic, large-scale company where I can make a significant impact.
        """)
st.subheader("Our Team")

col1, col2 , col3 = st.columns(3)

df = pandas.read_csv("data.csv")

with col1:
    for index, row in df[:4].iterrows():
        st.subheader(f'{row["first name"].title()} {row["last name"].title()}')
        st.write(row["role"])
        st.image("images/" + row["image"])

with col2:
    for index, row in df[4:8].iterrows():
        st.subheader(f'{row["first name"].title()} {row["last name"].title()}')
        st.write(row["role"])
        st.image("images/" + row["image"])

with col3:
    for index, row in df[8:].iterrows():
        st.subheader(f'{row["first name"].title()} {row["last name"].title()}')
        st.write(row["role"])
        st.image("images/" + row["image"])