import os
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from langchain.document_loaders import PyPDFLoader
import pandas as pd
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.document_loaders import PyPDFLoader, DirectoryLoader
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain.pydantic_v1 import BaseModel, Field

def process_papers_from_drive(download_dir, output_csv):
    """
    Processes each PDF file in the download directory using LangGraph 
    and saves results to a CSV file.
    """
    pdf_files = [os.path.join(download_dir, f) for f in os.listdir(download_dir) if f.endswith('.pdf')]

    results = []
    for i, file_path in enumerate(pdf_files):
        print(f"Processing file {i + 1}/{len(pdf_files)}: {file_path}")

        loader = PyPDFLoader(file_path)
        documents = loader.load()

        doc_text = " ".join([doc.page_content for doc in documents])
        sanitized_text = doc_text.replace("{", "{{").replace("}", "}}")

        result = report_decider(sanitized_text)
        print(result)
        results.append({"File": os.path.basename(file_path), "Result": result})

    df = pd.DataFrame(results)
    df.to_csv(output_csv, index=False)
    print(f"Results saved to {output_csv}")


def report_decider(doc):
    print(doc[:100]) 
    
    class decide(BaseModel):
        Binary_Score: str = Field(..., description="Is this Report Publishable?, respond with Yes or No.")

    GOOGLE_API_KEY = "AIzaSyAEqCEpjV4_6nZFKGQv8cxiyffiUNdDjGE"
    llm = ChatGoogleGenerativeAI(api_key = GOOGLE_API_KEY, model = "gemini-1.5-flash",temperature = 0.1)
    
    structured_llm = llm.with_structured_output(decide)
    
    system = """
    You are an AI system tasked with determining whether a given document is a publishable research paper. A publishable research paper must meet the following criteria:

    1. Structure:
    - The document includes a title, abstract, introduction, methodology, results, discussion, and references.
    
    2. **Content**:
    - The document presents original research, analysis, or findings.
    - It has a clear research question, hypothesis, or objective.
    - The methodology is well-detailed and appropriate for the research question.
    - Results are presented with supporting data, graphs, or tables.

    3. **Language and Formatting**:
    - The writing is clear, concise, and follows academic standards.
    - Proper citations and references are included in a recognized citation style.

    4. **Credibility**:
    - Sources cited in the references are credible and relevant to the topic.
    - The claims made are supported by sufficient evidence.

    Your task is to analyze the provided document and respond with "Yes" if it meets these criteria for publication or "No" if it does not.

    Document: {doc}
    """  
    
    binary_prompt = ChatPromptTemplate.from_messages(
        [
            ("system", system),
            ("human", f"paper: {doc}")
        ]
    )
        
    grader_chain = binary_prompt | structured_llm
    
    try:
        llm_response = grader_chain.invoke({"doc": doc})
        print("LLM Response received successfully.")
        
        prediction_output = llm_response.Binary_Score
        return prediction_output
    except Exception as e:
        print(f"Error during LLM invocation: {e}")
        return {"prediction": None}