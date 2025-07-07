# backend/qa_engine.py
import os
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAI
from langchain_core.prompts import PromptTemplate

load_dotenv()

llm = GoogleGenerativeAI(
    model="models/gemini-1.5-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    convert_system_message_to_human=True
)

class QAEngine:
    def __init__(self, document_text: str):
        # Limit to 12000 characters to stay within Gemini token limits
        self.document_text = document_text[:12000]

    def ask(self, query: str):
        template = """
        You are a document reasoning assistant.

        Use only this document to answer the question:

        {document}

        Question: {query}

        Justify your answer with quotes from the document.
        """
        prompt = PromptTemplate.from_template(template)
        full_prompt = prompt.format(document=self.document_text, query=query)

        response = llm.invoke(full_prompt)
        return response.strip(), [self.document_text]
