# chat.py — Application logic layer: manages chat interactions and conversation memory.

from gemini import GeminiClient

class ChatSession:
    # Stores and manages the conversation history for a single chat session.

    def __init__(self) -> None:
        # History is a list of turns, each matching the Gemini API message format
        self._history: list[dict] = []

    def add_user_message(self, text: str) -> None:
        # Appends a user turn to the conversation history.
        self._history.append({
            "role": "user",
            "parts": [{"text": text}]
        })

    def add_model_response(self, text: str) -> None:
        # Appends a model turn to the conversation history.
        self._history.append({
            "role": "model",
            "parts": [{"text": text}]
        })

    def get_history(self) -> list[dict]:
        # Returns the full conversation history.
        return self._history
    
    def clear(self) -> None:
        # Resets the conversation history.
        self._history.clear()

class ChatService:
    # Coordinates user messages, conversation history, and AI responses.

    def __init__(self) -> None:

        self._client = GeminiClient()
        self._session = ChatSession()

    def chat(self, user_message: str) -> str:

        if not user_message.strip():
            raise ValueError("User message must not be empty.")
        
        # Record the user's message before sending
        self._session.add_user_message(user_message)

        # Pass the full history so Gemini has context for its reply
        response = self._client.generate_response(self._session.get_history())

        # Record the model's reply to keep the history complete
        self._session.add_model_response(response)

        return response
    
    def clear_history(self) -> None:
        # Clears the current conversation so a fresh session can begin.
        self._session.clear()