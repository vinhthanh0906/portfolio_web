import streamlit as st
from forms.contact import contact_form


@st.dialog("Contact me")
def show_contact_form():
    contact_form()

col1, col2 = st.columns(2, gap="small",vertical_alignment="center")
with col1:
    st.image("D:\WORK\Python\web\portfolio_web\img\images.jpeg", width= 230)

with col2:
    st.title("Vinch", anchor= False)
    st.write(
        "Passion, B*tch!"
    )
    if st.button("Contact Me: "):
        show_contact_form()
        
# -------EXPERIENCE & QUALIFICATIONA ------
st.write("\n")
st.subheader("Experiance  & Qualifications", anchor=False)
st.write("""
        - 1 Years experiance extracting actionable insights from da
        - Strong hands-on experiance and knowledge in Python and Game
        - Good understanding  of statistical principles and their respective applications
        - Excellent team-player and displating a strong sense of initative on taks
        """)


st.subheader("Skills")
st.write("""
        - Programming Language: Python, C++, C
        - Python Library: Scikit-Learn, Pytorch, Tensorflow
        - Modeling: Linear Regression, K-means, Neural Network
        - Database: MySql
        - Streamlit, Flask
        """)


st.write("\n")