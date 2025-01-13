## THIS IS A STREAMLIT APP FOR TASK-2:
import streamlit as st
from src.conference_classification import classify_conference
from langchain.document_loaders import PyPDFLoader
import tempfile

st.title("Conference Classifier")
st.write("""
This application classifies research papers into one of the following conferences:
**CVPR, NeurIPS, EMNLP, TMLR, KDD**. 
Upload a PDF or paste the content of your document to get started.
""")

# File Upload or Text Input
uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])
text_input = st.text_area("Or paste the document content here")

if st.button("Classify"):
    if uploaded_file:
        st.info("Processing uploaded PDF...")
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_file:
            temp_file.write(uploaded_file.read())
            temp_file_path = temp_file.name

        loader = PyPDFLoader(temp_file_path)
        documents = loader.load()

        doc_text = " ".join([doc.page_content for doc in documents])
        sanitized_text = doc_text.replace("{", "{{").replace("}", "}}")
        result = classify_conference(sanitized_text)
        st.write(result)
    elif text_input.strip():
        sanitized_text = text_input.replace("{", "{{").replace("}", "}}")
    else:
        st.error("Please upload a PDF or enter document content!")
        st.stop()

    st.info("Classifying the document...")
