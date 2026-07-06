# config.py — Loads and validates environment variables for the AI Chat App.

import os
from dotenv import load_dotenv

# Load variables from the .env file into the environment
load_dotenv()

def get_api_key() -> str:
    # Reads and returns the Gemini API key from the environment.
    
    api_key: str = os.getenv("GEMINI_API_KEY", "")

    if not api_key:
        raise ValueError(
            "Missing GEMINI_API_KEY. "
            "Please add it to your .env file: GEMINI_API_KEY=your_key_here"
            )
    
    return api_key

GEMINI_API_KEY = get_api_key()