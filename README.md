# 🧠 GenAI Document Assistant

## Features
- Upload documents (PDF or TXT)
- Auto-summary (≤150 words)
- Ask any question with document-grounded answers
- Challenge mode with logic questions + feedback
- Justified answers with source snippet

## Setup
```bash
git clone https://github.com/yourusername/genai-doc-assistant.git
cd genai-doc-assistant
pip install -r requirements.txt
echo "OPENAI_API_KEY=your_key_here" > .env
streamlit run frontend/streamlit_app.py


"""
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/widerdev/-Smart-Assistant-for-Research-Summarization-.git
git push -u origin main
"""