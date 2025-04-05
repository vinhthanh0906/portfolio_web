import streamlit as st
import numpy as np
import pandas as pd

from forms.contact import contact_form
st.title("Welcome to Facebook")


col1,col2 = st.columns(2, gap="small", vertical_alignment="center")
about_page = st.Page(
    page = "D:\WORK\Python\web\portfolio_web\others\info.py",
    title= "About Me",
    icon = ":material/account_circle:",
    default = True,
)


project_1_page = st.Page(
    page = "D:\WORK\Python\web\portfolio_web\others\chatbot.py",
    title = "Chatbot",
    icon = ":material/bar_chart:",
)


project_2_page = st.Page(
    page = "D:\WORK\Python\web\portfolio_web\others\game.py",
    title= "Flappy Bird",
    icon = ":material/smart_toy:",)

#Navigation setup
pg = st.navigation({"Info":[about_page],
                    "Projects ": [project_1_page, project_2_page]
                    })


#Shared on all page
st.logo("img/logo.jpg")
st.sidebar.text("Made by Thanh Vinh")
pg.run()