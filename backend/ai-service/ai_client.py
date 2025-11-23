import os
from typing import List

import google.generativeai as genai

# For API Key Management, it's recommended to use environment variables.
# The user should set the GOOGLE_API_KEY environment variable.
# Example: export GOOGLE_API_KEY="YOUR_API_KEY"
genai.configure(api_key=os.environ.get("GOOGLE_API_KEY"))

# Initialize the generative model
model = genai.GenerativeModel('gemini-pro')

def generate_summary(text_chunks: List[str]) -> str:
    """
    Generates a summary from a list of text chunks using the Gemini API.
    """
    if not text_chunks:
        return ""

    full_text = " ".join(text_chunks)
    
    prompt = f"""
    Please provide a concise summary of the following text. 
    The summary should capture the main ideas and key points of the document.

    Text:
    ---
    {full_text}
    ---
    """
    
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        print(f"Error generating summary from AI service: {e}")
        # Depending on the desired error handling, you might want to return a specific error message
        # or just an empty string. For now, we re-raise the exception to be handled by the caller.
        raise
