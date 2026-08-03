# chat.py — Application logic layer: manages chat interactions and conversation memory.

from gemini import GeminiClient
from prompts import DEFAULT_SYSTEM_PROMPT

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

        self._system_prompt = DEFAULT_SYSTEM_PROMPT

    def _build_payload(self) -> list[dict]:
        # Combines the system prompt and conversation history into a single list ready to be sent to GeminiClient.

        system_turn: list[dict] = [
            # Present the system prompt as a user instruction
            {"role": "user", "parts": [{"text": self._system_prompt}]},

            # Model acknowledges, establishing the instruction as accepted
            {"role": "model", "parts": [{"text": "Understood."}]}
        ]

        return system_turn + self._session.get_history()

    def chat(self, user_message: str) -> str:

        if not user_message.strip():
            raise ValueError("User message must not be empty.")
        
        # Record the user's message before sending
        self._session.add_user_message(user_message)

        # Build the full payload: system prompt + conversation history
        payload = self._build_payload()

        # Pass the full history so Gemini has context for its reply
        response = self._client.generate_response(payload)

        # Record the model's reply to keep the history complete
        self._session.add_model_response(response)

        return response
    
    def clear_history(self) -> None:
        # Clears the current conversation so a fresh session can begin.
        self._session.clear()