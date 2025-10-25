# Importing necessary libraries
import os
import google.generativeai as genai
import streamlit as st

st.header("Gemini Chat Bot")
st.title("Generate text using Google Gemini Model")
# Setting the API key for Google Generative AI
API=st.secrets["GOOGLE_API_KEY"]
genai.configure(api_key = API)

# Function to generate a response from the chatbot
user_input=st.text_area("Provide the prompt",'Hello, how are you?')
model= genai.GenerativeModel("gemini-2.0-flash")
if st.button("Generate Response"):
   response = model.generate_content(user_input)
   st.success("Answer{}".format(response.text))