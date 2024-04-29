'''

from pdf_extractor import extract_text_from_pdf
from ocr import perform_ocr
from ner import perform_ner, visualize_entities
from qa import perform_qa


def main():
    st.title("Document Processing Application")

    # Sidebar for selecting document type
    document_type = st.sidebar.radio("Select Document Type:", ("Manual Text", "PDF", "Image"))

    text = ""  # Initialize text variable

    if document_type == "Manual Text":
        st.sidebar.write("You selected Manual Text")
        # Text input field for manual input
        manual_text = st.text_area("Enter text here:", "")
        text = manual_text.strip()  # Set text variable to manual_text

    elif document_type == "PDF":
        st.sidebar.write("You selected PDF")
        # Upload PDF file
        uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

        if uploaded_file is not None:
            text = extract_text_from_pdf(uploaded_file)
            st.write("Extracted text:")
            st.write(text)

    elif document_type == "Image":
        st.sidebar.write("You selected Image")
        # Get the input image from the user
        input_image = get_image()

        if input_image:
            # Perform OCR on the image
            text = perform_ocr(input_image)
            st.header("OCR Text Extraction Results:")
            st.write(text)

    # Entity Recognition section
    if st.sidebar.button("Entity Recognition"):
        if text:
            st.sidebar.subheader("Automated Entity Recognition:")
            doc_med7, doc_bc5cdr, combined_entities = perform_ner(text)
            html = visualize_entities(doc_med7, combined_entities)
            st.write(html, unsafe_allow_html=True)
        else:
            st.warning("Please input some text before performing entity recognition.")

    # Question Answering section
    st.sidebar.markdown("---")
    st.header("Question Answering")
    question = st.text_input("Enter your query:")
    if st.button("Search"):
        if text:
            if question:
                answer = perform_qa(question, text)
                st.subheader("Answer:")
                st.write(answer)
            else:
                st.warning("Please enter a query before searching.")
        else:
            st.warning("Please input some text before querying.")


if __name__ == "__main__":
    main()
'''
import streamlit as st
from pdf_extractor import extract_text_from_pdf
from ocr import get_image, perform_ocr
from ner import perform_ner, visualize_entities
from qa import perform_qa


def main():
    st.title("Document Processing Application")

    # Sidebar for selecting document type
    document_type = st.sidebar.radio("Select Document Type:", ("Manual Text", "PDF", "Image"))

    text = ""  # Initialize text variable

    if document_type == "Manual Text":
        st.sidebar.write("You selected Manual Text")
        # Text input field for manual input
        manual_text = st.text_area("Enter text here:", "")
        text = manual_text.strip()  # Set text variable to manual_text

    elif document_type == "PDF":
        st.sidebar.write("You selected PDF")
        # Upload PDF file
        uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

        if uploaded_file is not None:
            text = extract_text_from_pdf(uploaded_file)
            st.write("Extracted text:")
            st.write(text)

    elif document_type == "Image":
        st.sidebar.write("You selected Image")
        # Get the input image from the user
        input_image = get_image()

        if input_image:
            # Perform OCR on the image
            text = perform_ocr(input_image)
            st.header("OCR Text Extraction Results:")
            st.write(text)

    # Entity Recognition section
    if st.sidebar.button("Entity Recognition"):
        if text:
            st.sidebar.subheader("Automated Entity Recognition:")
            doc_med7, doc_bc5cdr, combined_entities = perform_ner(text)
            html = visualize_entities(doc_med7, combined_entities)
            st.write(html, unsafe_allow_html=True)
        else:
            st.warning("Please input some text before performing entity recognition.")

    # Question Answering section
    st.sidebar.markdown("---")
    st.header("Question Answering")
    question = st.text_input("Enter your query:")
    if st.button("Search"):
        if text:
            if question:
                answer = perform_qa(question, text)
                st.subheader("Answer:")
                st.write(answer)
            else:
                st.warning("Please enter a query before searching.")
        else:
            st.warning("Please input some text before querying.")


if __name__ == "__main__":
    main()
