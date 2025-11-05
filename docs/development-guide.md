# Development Guide

## Prerequisites
- Python 3.9+
- A Google Firebase project.
- API keys for Google Gemini and OpenAI.

## Setup Commands
```bash
# 1. Clone the repository
git clone <repository_url>

# 2. Create a virtual environment
python -m venv venv
source venv/bin/activate

# 3. Install the dependencies
pip install -r requirements.txt

# 4. Run the application
uvicorn main:app --reload
```