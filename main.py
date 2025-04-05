import streamlit as st
import numpy as np
import pandas as pd

st.title("Welcome to Facebook")

about_page = st.Page(
    page = "view/about_me.py",
    title= "About Me",
    icon = ":material/account_circle: ",
    default = True,
)


project_1_page = st.Page(
    page = "view/chatbot.py",
    title = "Chatbot",
    icon = ":material/bar_chart:",
)


project_2_page = st.Page(
    page = "view/flappybird.py",
    title= "Flappy Bird",
    icon = ":material/smart_toy:",)


pg = st.navigation({"Info":[about_page],
                   "Projects ": [project_1_page, project_2_page]
                   })


pg.run()