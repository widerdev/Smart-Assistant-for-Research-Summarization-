# backend/summarizer.py
import os
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAI

load_dotenv()

llm = GoogleGenerativeAI(
    model="models/gemini-1.5-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    convert_system_message_to_human=True
)

def summarize_text(text):
    input_prompt = f"""
    Summarize the following document clearly in 4-6 sentences:

    {text[:12000]}
    """

    response = llm.invoke(input_prompt)
    return response.strip()
