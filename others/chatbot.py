import streamlit as st

st.title("🤖 Simple Rule-Based Chatbot")

# Define some canned responses
bot_responses = {
    "hi": "Hello! 👋 How can I help you today?",
    "hello": "Hey there! What can I do for you?",
    "how are you": "I'm just code, but I'm running great! 😄",
    "what is your name": "I'm ChatSimple, your rule-based buddy!",
    "bye": "Goodbye! 👋 Have a great day!",
}

# Store chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Chat input box
user_input = st.chat_input("Type your message here...")

if user_input:
    st.session_state.chat_history.append(("user", user_input))

    # Normalize input to match keys (simple lowercase match)
    cleaned_input = user_input.strip().lower()

    # Get bot response or default fallback
    response = bot_responses.get(cleaned_input, "Sorry, I don't understand that yet. 🤖")

    st.session_state.chat_history.append(("bot", response))

# Display chat history
for sender, message in st.session_state.chat_history:
    with st.chat_message(sender):
        st.markdown(message)
