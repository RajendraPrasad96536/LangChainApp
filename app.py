from langchain.llms import OpenAI
from dotenv import load_dotenv

load_dotenv() 

import streamlit as st
import os

## Function to load OpenAI model and get responses

def get_openai_response(question):
    llm =  OpenAI(openai_api_key=os.getenv("OPEN_API_KEY"), model_name="text-davinci-003", temperature=0.6)
    response = llm(question)
    return response

# Initalize streamlit app
    
st.set_page_config(page_title="Q&A Demo")

st.header("Langchain Application")

input = st.text_input("Input: ", key="input")

response  = get_openai_response(input)

submit = st.button("Ask the question")

# If ask button is clicked

if submit:
    st.subheader("The response is ")
    st.write(response)
