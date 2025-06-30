import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
GROQ_API_KEY = os.getenv('GROQ_API_KEY')

def get_summary_from_llm(text):
    prompt = f"Summarize the following document:\n\n{text[:5000]}"  # Truncate if needed
    response = requests.post(
        "https://api.groq.com/openai/v1/chat/completions",  # adjust based on actual Groq API
        headers={
            "Authorization": f"Bearer {GROQ_API_KEY}",  
            "Content-Type": "application/json"
        },
        json={
            "model": "meta-llama/llama-4-scout-17b-16e-instruct",  # example model
            "messages": [{"role": "user", "content": prompt}]
        }
    )
    return response.json()['choices'][0]['message']['content']
