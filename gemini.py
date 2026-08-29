# gemini.py — Service layer for interacting with the Gemini API.

from google import genai

from config import GEMINI_API_KEY

class GeminiClient:
    """Handles all communication with the Gemini API."""

    MODEL_NAME = "gemini-2.5-flash"

    def __init__(self) -> None:
        if not GEMINI_API_KEY:
            raise ValueError(
                "GEMINI_API_KEY is missing. "
                "Set it in your .env file or environment variables."
            )

        self._client = genai.Client(api_key=GEMINI_API_KEY)

    def generate_response(self, history: list[dict]) -> str:
        """
        Generate a response from Gemini using conversation history.

        Expected history format:
        [
            {"role": "user", "parts": [{"text": "Hello"}]},
            {"role": "model", "parts": [{"text": "Hi! How can I help?"}]},
            {"role": "user", "parts": [{"text": "Tell me a joke."}]},
        ]
        """

        if not history:
            raise ValueError("Conversation history must not be empty.")

        try:
            response = self._client.models.generate_content(
                model=self.MODEL_NAME,
                contents=history,
            )

            if not response.text:
                raise RuntimeError(
                    "Gemini returned an empty response."
                )

            return response.text

        except Exception as e:
            # Keep API-specific errors from leaking into the rest
            # of the application.
            raise RuntimeError(
                f"Gemini API error: {e}"
            ) from e