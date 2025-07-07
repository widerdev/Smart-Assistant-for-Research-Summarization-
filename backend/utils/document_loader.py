import fitz  # PyMuPDF

def extract_text_from_pdf(uploaded_file):
    with fitz.open(stream=uploaded_file.read(), filetype="pdf") as doc:
        return "\n".join(page.get_text() for page in doc)

def extract_text_from_txt(uploaded_file):
    return uploaded_file.read().decode("utf-8")