from PyPDF2 import PdfReader
import docx

def extract_text_from_file(filepath):
    if filepath.endswith('.pdf'):
        reader = PdfReader(filepath)
        return "\n".join(page.extract_text() for page in reader.pages if page.extract_text())
    elif filepath.endswith('.docx'):
        doc = docx.Document(filepath)
        return "\n".join([p.text for p in doc.paragraphs])
    elif filepath.endswith('.txt'):
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    return ""
