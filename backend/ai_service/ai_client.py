import os
import json
from typing import List, Dict, Any

import google.generativeai as genai

# For API Key Management, it's recommended to use environment variables.
# The user should set the GOOGLE_API_KEY environment variable.
# Example: export GOOGLE_API_KEY="YOUR_API_KEY"
genai.configure(api_key=os.environ.get("GOOGLE_API_KEY"))

# Initialize the generative model
model = genai.GenerativeModel('gemini-pro-latest')

def _strip_markdown_json(text: str) -> str:
    """Strips markdown code block syntax from a string containing JSON."""
    if text.startswith("```json") and text.endswith("```"):
        return text[7:-3].strip()
    return text

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

def generate_flashcards(text_chunks: List[str]) -> List[Dict[str, str]]:
    """
    Generates flashcards from a list of text chunks using the Gemini API.
    The AI is instructed to return flashcards in a JSON array format.
    """
    if not text_chunks:
        return []

    full_text = " ".join(text_chunks)

    prompt = f"""
    Please generate a list of flashcards (question and answer pairs) from the following text.
    Each flashcard should consist of a 'front' (question) and a 'back' (answer).
    Return the flashcards as a JSON array of objects, where each object has 'front' and 'back' keys.

    Example format:
    [
      {{"front": "Question 1", "back": "Answer 1"}},
      {{"front": "Question 2", "back": "Answer 2"}}
    ]

    Text:
    ---
    {full_text}
    ---
    """

    try:
        response = model.generate_content(prompt)
        # Strip markdown before decoding JSON
        cleaned_response_text = _strip_markdown_json(response.text)
        flashcards = json.loads(cleaned_response_text)
        return flashcards
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON from AI for flashcards: {e}")
        print(f"AI response text: {response.text}")
        raise
    except Exception as e:
        print(f"Error generating flashcards from AI service: {e}")
        raise

def generate_quiz(text_chunks: List[str]) -> List[Dict[str, Any]]:
    """
    Generates a quiz from a list of text chunks using the Gemini API.
    The AI is instructed to return quiz questions in a JSON array format.
    """
    if not text_chunks:
        return []

    full_text = " ".join(text_chunks)

    prompt = f"""
    Please generate a multiple-choice quiz from the following text.
    Each question should have a 'question', a list of 'options', and an 'answer' (the correct option).
    Return the quiz as a JSON array of objects.

    Example format:
    [
      {{
        "question": "What is the capital of France?",
        "options": ["Berlin", "Madrid", "Paris", "Rome"],
        "answer": "Paris"
      }},
      {{
        "question": "Which planet is known as the Red Planet?",
        "options": ["Earth", "Mars", "Jupiter", "Venus"],
        "answer": "Mars"
      }}
    ]

    Text:
    ---
    {full_text}
    ---
    """

    try:
        response = model.generate_content(prompt)
        # Strip markdown before decoding JSON
        cleaned_response_text = _strip_markdown_json(response.text)
        quiz = json.loads(cleaned_response_text)
        return quiz
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON from AI for quiz: {e}")
        print(f"AI response text: {response.text}")
        raise
    except Exception as e:
        print(f"Error generating quiz from AI service: {e}")
        raise
