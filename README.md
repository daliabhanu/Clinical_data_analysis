# Clinical_data_analysis
Handling Doctor's Hand prescription into understandable text by identifying proper drug and disease.
## Overview

The Clinical Data Analysis Application is a Python-based tool developed to process and analyze doctors' prescriptions using natural language processing (NLP) techniques. This application aims to extract essential information from prescription documents, such as drug names, dosages, and diseases, and provide useful insights for healthcare professionals.

## Features

### Document Input Options

- **Manual Text Input:** Users can manually enter prescription text into the application.
- **PDF Upload:** Support for uploading PDF files containing prescription data.
- **Image Upload:** Ability to upload images containing prescription information for OCR (Optical Character Recognition).

### Data Processing and Analysis

- **Entity Recognition:** The application utilizes SpaCy for named entity recognition (NER) to identify drugs, dosages, and diseases mentioned in the prescriptions.
- **Question Answering:** A question answering module powered by transformer-based models allows users to query specific information about the prescription content.

## Installation

To run the application locally, follow these steps:

1. **Clone Repository:**
   ```bash
   git clone https://github.com/your-username/clinical-data-analysis.git
Install Dependencies:
bash
Copy code
pip install -r requirements.txt
Run Application:
bash
Copy code
streamlit run main.py
Access Application:
Open your web browser and navigate to http://localhost:8501 to access the application.
Usage
Select Document Type:
Choose the appropriate document type (Manual Text, PDF, or Image) from the sidebar.
Input Prescription Data:
For manual text input, enter the prescription text into the provided text area.
For PDF or image upload, use the respective file upload option to provide prescription documents.
Perform Analysis:
Use the Entity Recognition button to identify drugs, dosages, and diseases mentioned in the prescription.
Utilize the Question Answering section to ask specific queries about the prescription content.
Streamlit: Python library for building interactive web applications.
SpaCy: Python library for NLP tasks, including entity recognition.
PyPDF2: Python library for reading and extracting text from PDF files.
TensorFlow: Deep learning framework used for question answering module.
Transformer Models: Hugging Face Transformers library for transformer-based NLP tasks.
This README provides an in-depth overview of the application, including its features, installation instructions, usage guidelines, license information, and credits to the libraries and frameworks used. Adjust the content as needed to match the specifics of your project.
