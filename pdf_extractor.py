from PyPDF2 import PdfReader
import tempfile
import os
import streamlit as st

def extract_text_from_pdf(uploaded_file):
    text = ""
    with st.spinner("Extracting text..."):
        with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
            tmp_file.write(uploaded_file.read())
            tmp_file.seek(0)
            pdf_path = tmp_file.name

        with open(pdf_path, "rb") as file:
            reader = PdfReader(file)
            for page_num in range(len(reader.pages)):
                page = reader.pages[page_num]
                text += page.extract_text()

        os.unlink(pdf_path)  # Remove temporary PDF file

    return text
