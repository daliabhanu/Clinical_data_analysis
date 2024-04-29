import streamlit as st
import keras_ocr

def get_image():
    uploaded_file = st.file_uploader("Upload Image File", type=['jpg', 'jpeg', 'png'])
    if uploaded_file is not None:
        return uploaded_file
    else:
        return None

def perform_ocr(image):
    pipeline = keras_ocr.pipeline.Pipeline()
    predictions = pipeline.recognize([image])[0]
    text = ' '.join([text for text, _ in predictions])
    return text
