import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)


with col1:
    st.image("images/profile_photo.png", width=450)


with col2:
    st.title("Scott Caruso")
    content = """
    One of my greatest passions lies in the realm of technology and software development. As an avid Python enthusiast, I thrive on the art of crafting innovative applications. Whether it's building intuitive user interfaces or implementing intricate algorithms, I immerse myself in the world of coding. The process of transforming ideas into tangible software brings me immense joy and a sense of accomplishment.
    """
    st.info(content)


content2 = """
Below you can find some of the apps I have built in Python. Feel free to contact me!"""

st.write(content2)

col3, col4 = st.columns(2)

df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])