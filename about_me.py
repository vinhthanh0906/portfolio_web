import streamlit as st

@st.experimental_dialog("Contact me")
def show_contact_form():
    st.text_input("First Name")

col1, col2 = st.columns(2, gap="small",vertical_alignment="center")
with col1:
    st.image("/Users/nguyenthanhvinh/Documents/PYTHON/portfolio_web/assets/images.jpeg", width= 230)

with col2:
    st.title("Mark Zuchkerberg", anchor= False)
    st.write(
        "Lmao, assis"
    )
    if st.button("Goi cho toi: "):
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


st.write("\n")