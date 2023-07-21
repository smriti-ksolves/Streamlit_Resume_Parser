import streamlit as st
from pathlib import Path
import os
import pandas as pd
from Streamlit_Resume_Parser.extraction_data import file_extract
from Streamlit_Resume_Parser.question_generator import Generator
st.title("Question Generator")

text = st.empty()
st.header('Restricted File Extensions',)
uploaded_files = st.file_uploader('Upload your files',
 accept_multiple_files=True, type=['pdf','jpg','png','jpeg'])
quest_input = st.text_input("Enter your Question")

for file in uploaded_files:
    save_folder = 'pdfs'
    save_path = Path(save_folder, file.name)
    with open(save_path, mode='wb') as w:
        w.write(file.getvalue())
    path = os.path.join(save_folder,file.name)
    destination_path = f"pdfs/{file.name[:-4]}.txt"
    file_type = file.type
    file_extract(file_path=path,file_type=file_type,destination_path=destination_path)
    if quest_input:
        message = Generator(quest_input ,destination_path)
        st.write(message["message"])
    else:
        st.warning("Please enter a question")
    os.remove(destination_path)
    os.remove(path)