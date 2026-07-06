"""
app.py — Entry point for the AI Chat App.
Handles the CLI loop and wires all components together.
"""

from chat import ChatService

def main() -> None:
    # Starts the chat application and runs the interactive CLI loop.

    chat_service = ChatService()

    print("=" * 40)
    print("  Welcome to AI Chat App!")
    print("  Type 'exit' or 'quit' to leave.")
    print("=" * 40)

    while True:
        try:
            user_input = input("\nYou: ").strip()

            # Skip empty input without sending anything to the API
            if not user_input:
                continue

            # Exit cleanly on known quit commands
            if user_input.lower() in {"exit", "quit"}:
                print("Goodbye! 👋")
                break

            response = chat_service.chat(user_input)
            print(f"\nAI: {response}")

        except KeyboardInterrupt:
            # Handle Ctrl+C gracefully without a traceback
            print("\nGoodbye! 👋")
            break

        except Exception as e:
            # Catch unexpected errors and keep the loop running
            print(f"\n[Error] Something went wrong: {e}")


if __name__ == "__main__":
    main()