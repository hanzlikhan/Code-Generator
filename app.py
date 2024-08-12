import streamlit as st
import openai
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')

def generate_code(prompt, language):
    # Use the new ChatCompletion API for more advanced features
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": f"You are a helpful assistant that generates {language} code."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=150,
        temperature=0.5,
    )
    return response['choices'][0]['message']['content'].strip()

# Streamlit app interface
st.title("Advanced Code Generator App")
st.write("This app generates code snippets based on user input using OpenAI's GPT model.")

language = st.selectbox("Choose a programming language", ["Python", "JavaScript", "Java", "C++"])
prompt = st.text_input("Enter the task or algorithm you want code for", "e.g., Quick Sort Algorithm")

if st.button("Generate Code"):
    with st.spinner("Generating code..."):
        code = generate_code(prompt, language)
    st.code(code, language=language.lower())
