from flask import Flask, request, jsonify, render_template
from werkzeug.utils import secure_filename
import os
from utils.extract_text import extract_text_from_file
from utils.summarizer import get_summary_from_llm

app = Flask(__name__, static_url_path="/static", static_folder="static", template_folder="templates")
app.config['UPLOAD_FOLDER'] = 'uploads'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarize():
    try:
        text = request.form.get('raw_text', '').strip()
        file = request.files.get('document')

        if file and not text:
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            text = extract_text_from_file(filepath)

        if not text:
            return jsonify({'error': 'Please upload a document or enter some text.'}), 400

        # print(f"Extracted text: {text[:30]}...")  # Debugging line to check extracted text
        summary = get_summary_from_llm(text)
        return jsonify({'summary': summary})

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
    app.run(debug=True,host='0.0.0.0',port=3000)
