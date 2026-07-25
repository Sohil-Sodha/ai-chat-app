# gemini.py — Service layer for interacting with the Gemini API.

import google.generativeai as genai
from google.api_core.exceptions import GoogleAPIError

from config import GEMINI_API_KEY

class GeminiClient:
    # Handles all communication with the Gemini API.

    def __init__(self) -> None:

        # Configure the SDK with the API key from config.py
        genai.configure(api_key=GEMINI_API_KEY)
        self._model = genai.GenerativeModel(model_name="gemini-2.5-flash")

    def generate_response(self, history: list[dict]) -> str:

        if not history:
            raise ValueError("Conversation history must not be empty.")
        
        try:
            response = self._model.generate_content(history)
            return response.text
        
        except GoogleAPIError as e:
            raise RuntimeError(f"Gemini API error: {e}") from e