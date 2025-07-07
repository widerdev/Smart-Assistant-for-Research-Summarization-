# frontend/streamlit_app.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from backend.utils.document_loader import extract_text_from_pdf, extract_text_from_txt
from backend.summarizer import summarize_text
from backend.qa_engine import QAEngine

st.set_page_config(page_title="GenAI Document Assistant")
st.title("\U0001F4C4 GenAI Document Assistant")

uploaded_file = st.file_uploader("Upload a PDF or TXT file", type=["pdf", "txt"])

if uploaded_file:
    if uploaded_file.name.endswith(".pdf"):
        text = extract_text_from_pdf(uploaded_file)
    else:
        text = extract_text_from_txt(uploaded_file)

    st.subheader("\U0001F4DD Auto Summary")
    summary = summarize_text(text)
    st.info(summary)

    engine = QAEngine(text)
    mode = st.radio("Select a Mode", ["Ask Anything", "Challenge Me"])

    if mode == "Ask Anything":
        query = st.text_input("Type your question")
        if query:
            answer, sources = engine.ask(query)
            st.success("Answer: " + answer)
            st.code(sources[0][:500], language='markdown')

    elif mode == "Challenge Me":
        challenge_prompt = "Generate 3 logic-based comprehension questions from the document."
        questions, _ = engine.ask(challenge_prompt)
        st.markdown("### \U0001F9E0 Challenge Questions")
        for idx, q in enumerate(questions.strip().split("\n")):
            if q.strip():
                user_ans = st.text_input(q, key=f"q{idx}")
                if user_ans:
                    eval_prompt = f"Question: {q}\nUser's Answer: {user_ans}\nEvaluate this answer and provide feedback using the document."
                    feedback, _ = engine.ask(eval_prompt)
                    st.write("✅ Feedback:", feedback)


