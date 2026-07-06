# chat.py — Service layer that manages chat interactions.

from gemini import GeminiClient

class ChatService:
    # Coordinates user messages and AI responses via GeminiClient.

    def __init__(self) -> None:
        self._client = GeminiClient()

    def chat(self, user_message: str) -> str:

        if not user_message.strip():
            raise ValueError("User message must not be empty.")
        
        return self._client.generate_response(user_message)