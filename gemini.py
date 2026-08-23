# gemini.py — Service layer for interacting with the Gemini API.

import google.generativeai as genai
from google.api_core.exceptions import GoogleAPIError, Unauthenticated, ServiceUnavailable

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
        
        except Unauthenticated as e:
            # Raised when the API key is missing, revoked, or malformed
            raise PermissionError(
                "Invalid or missing API key. "
                "Check that GEMINI_API_KEY is set correctly in your .env file."
            ) from e
        
        except ServiceUnavailable as e:
            # Raised when the Gemini service cannot be reached
            raise ConnectionError(
                "Could not reach the Gemini API. "
                "Check your internet connection and try again."
            ) from e
        
        except GoogleAPIError as e:
            raise RuntimeError(f"Gemini API error: {e}") from e