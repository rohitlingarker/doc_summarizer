# 📄 Document Summarizer

A lightweight web app that summarizes uploaded documents or pasted text using Groq's LLM APIs. Built with a clean modern frontend and a Flask backend.

---

## 🧰 Tech Stack

| Layer        | Technology                         |
|--------------|------------------------------------|
| Frontend     | HTML, CSS, JavaScript, marked.js   |
| Backend      | Flask (Python)                     |
| LLM API      | Groq (e.g., Claude, LLaMA)         |
| File Parsing | PyMuPDF / textract (PDF, DOCX, etc.) |

---

## 🔧 Features

- Upload `.pdf`, `.docx`, `.txt`, etc. for summarization
- Paste raw text directly instead of uploading
- Clean and responsive UI
- Renders summaries in **Markdown**
- Uses Groq APIs to generate summaries

---

## 📁 Project Structure

```
project/
│
├── app.py                     # Main Flask application
├── utils/
│   ├── extract_text.py        # File text extractor
│   └── summarizer.py          # LLM summarizer logic
│
├── templates/
│   └── index.html             # Main HTML UI
│
├── static/
│   ├── style.css              # CSS for styling
│   └── script.js              # JS for form handling and markdown rendering
│
├── uploads/                   # Temp storage for uploaded files
└── README.md                  # Project documentation
```

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/doc-summarizer.git
cd doc-summarizer
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

> Example dependencies:
```txt
Flask
python-docx
PyMuPDF
requests
```

### 4. Set Up Groq API Key

Create a `.env` file or configure your API key securely:

```bash
export GROQ_API_KEY=your_api_key
```

### 5. Run the App

```bash
python app.py
```

App will be available at `http://localhost:5000`.

---

## 🌐 Usage

1. Visit the home page.
2. Upload a document or paste your text.
3. Click **Summarize**.
4. See the summary rendered in Markdown.

---

## 📄 Example Output

Markdown like:

```markdown
# Summary

- This document explains ...
- The main points are ...
- In conclusion ...
```

Is rendered beautifully using `marked.js` in the browser.

---

## 📦 API Overview

### `POST /summarize`

**Form data**:
- `document` (optional): file to upload
- `raw_text` (optional): plain text input

**Returns**:
```json
{
  "summary": "Markdown-formatted summary here..."
}
```

---

## 🔐 Security Note

- Files are stored temporarily in `uploads/` and should be purged periodically.
- Always validate file types and size if deploying publicly.
- Do **not expose** your Groq API key on the frontend.

---

## ✅ To-Do / Improvements

- Add support for OCR (images / scanned PDFs)
- Show loading spinner during summary generation
- Export summary as `.txt` or `.md`
- Add dark mode toggle
- Add history tab / past summaries

---

## 📃 License

MIT License. You are free to use, modify, and distribute.