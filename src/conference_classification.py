import os
from dotenv import load_dotenv
from langchain.schema import SystemMessage, HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI


def classify_conference(doc):
    load_dotenv()
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
    llm = ChatGoogleGenerativeAI(api_key = GOOGLE_API_KEY, model = "gemini-1.5-flash",temperature = 0.1)

    system_message = """
    You are an AI system tasked with determining whether a given document is publishable in one 
    of the following conferences: CVPR, NeurIPS, EMNLP, TMLR, and KDD.
    Each classification must be accompanied by a well-reasoned rationale of up to 100 words, explaining how the paper’s content, methodology,
    and findings correspond to the themes, focus areas, and quality standards of the
    chosen conference. This rationale will ensure that the paper is not only a good fit
    for the conference but also adheres to the academic criteria expected by these
    prestigious venues.
    """

    messages = [
        SystemMessage(content=system_message),
        HumanMessage(content=f"Paper: {doc}")
    ]

    try:
        response = llm.invoke(messages)
        print(response.content)
        return response.content
    except Exception as e:
        print(f"Error occurred: {e}")