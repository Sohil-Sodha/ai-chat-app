"""
app.py — Entry point for the AI Chat App.
Handles the CLI loop and wires all components together.
"""

from chat import ChatService
from utils import print_banner, formate_ai_response, print_goodbye

def main() -> None:
    # Starts the chat application and runs the interactive CLI loop.

    chat_service = ChatService()

    print_banner()

    while True:
        try:
            user_input = input("\nYou: ").strip()

            # Skip empty input without sending anything to the API
            if not user_input:
                continue

            # Exit cleanly on known quit commands
            if user_input.lower() in {"exit", "quit"}:
                print_goodbye()
                break

            response = chat_service.chat(user_input)
            print(formate_ai_response(response))

        except KeyboardInterrupt:
            # Handle Ctrl+C gracefully without a traceback
            print_goodbye()
            break

        except Exception as e:
            # Catch unexpected errors and keep the loop running
            print(f"\n[Error] Something went wrong: {e}")


if __name__ == "__main__":
    main()