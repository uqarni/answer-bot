from langchain.document_loaders import TextLoader
from langchain.indexes import VectorstoreIndexCreator
import streamlit as st
import os
import openai

openai.api_key = os.environ.get('OPENAI_API_KEY')

st.title("Document Bot")
uploaded_file = st.file_uploader("Choose a file")
filename = "text.txt"
if uploaded_file is not None:
    if os.path.exists(filename):
        os.remove(filename)
    with open(filename,"wb") as f:
        f.write(uploaded_file.getbuffer())
    st.success("File uploaded")

user_question = st.text_input(
    "Enter Your Question : ",
    placeholder = "Cyanobacteria can perform photosynthetsis , are they considered as plants?",
)

if st.button("Tell me about it", type = "primary"):
    loader = TextLoader('text.txt')
    index = VectorstoreIndexCreator().from_loaders([loader])
    query = user_question
    answer = index.query_with_sources(query)
    st.success(answer['answer'])




