import streamlit as st

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