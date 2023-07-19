import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, empty_col, col2 = st.columns([1.5,.5,1.5])


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

col3, empty_col,col4 = st.columns([1.5,.5,1.5])

df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write("[Source Code](github_link)")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write("[Source Code](github_link)")