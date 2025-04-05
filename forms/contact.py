import streamlit as st
import re
import requests


WEBHOOK_URL = st.secrets["WEBHOOK_URL"]

#Checking valid email

def is_valid_email(email):
    email_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(email_pattern, email) is not None

#Contact form
def contact_form():
    with st.form("contact_form"):
        name = st.text_input("First Name")
        email = st.text_input("Email")
        message = st.text_input("Your Message")
        submit_button = st.form_submit_button("Submit")
        
        if submit_button:
            if not WEBHOOK_URL:
                st.error("Incoming features")
                st.stop()
                
            if not name:
                st.error("Please enter your name")
                st.stop()
                
            if not message:
                st.error("Message box can not be empty")
                st.stop()
                
            if not is_valid_email(email):
                st.error("Please enter valid email")
                st.stop()
            
            if not email:
                st.error("Please enter your email")
                st.stop()
                
            #Prepare the data payload and send it to the specified webhook URL
            
            data = {"email": email, "name": name, "message": message}
            response = requests.post(WEBHOOK_URL, json=data)
            
            if response.status_code == 200:
                st.success("Message successfully sent!")
            else:
                st.error("Sending error, try again")
            
                
            
            
            