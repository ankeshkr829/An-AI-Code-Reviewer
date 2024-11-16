import streamlit as st
import google.generativeai as ai

# Configure the Google Generative AI API



api_key = st.secrets["general"]["api_key"]
ai.configure(api_key=api_key)    
    
# Set up the app layout
st.title("An AI Code Reviewer")
st.write("Enter your Python code below for review:")

# Text area for code input
user_code = st.text_area("Enter your Python code here...", height=200)

# Button to trigger code review
if st.button("Generate"):
    if user_code:
        # Initialize the generative model
        llm = ai.GenerativeModel("models/gemini-1.5-flash")
        
        # Send the user code for review
        chatbot = llm.start_chat(history=[])
        response = chatbot.send_message(f"Review the following Python code and identify any bugs:\n{user_code}")
        
        # Display the AI-generated response
        st.subheader("Code Review")
        st.write("Bug Report:")
        st.write(response.text)  # Display AI response