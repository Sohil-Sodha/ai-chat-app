"""
app.py — Entry point for the AI Chat App.
Handles the CLI loop and wires all components together.
"""

from chat import ChatService
from utils import print_banner, formate_ai_response, print_goodbye

def main() -> None:
    # Starts the chat application and runs the interactive CLI loop.

    # Initialising ChatService here also triggers config.py and gemini.py setup,
    # so an invalid API key is caught before the loop even starts.

    try:
        chat_service = ChatService()
    
    except PermissionError as e:
        print(f"\n[Configuration Error]: {e}")
        return
    
    except Exception as e:
        print(f"\n[Startup Error] Could not start the app: {e}")
        return

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

        except ValueError as e:
            # Empty or invalid input — no need to crash the loop
            print(f"\n[Input Error] {e}")

        except PermissionError as e:
            # API key became invalid mid-session — unrecoverable, exit cleanly
            print(f"\n[Authentication Error] {e}")
            break

        except ConnectionError as e:
             # Network issue — recoverable, let the user try again
             print(f"\n[Connection Error] {e}")

        except RuntimeError as e:
            # Unexpected API failure — show the error, keep the loop running
            print(f"\n[API Error] {e}")

        except KeyboardInterrupt:
            # Handle Ctrl+C gracefully without a traceback
            print_goodbye()
            break

        except Exception as e:
            # Catch unexpected errors and keep the loop running
            print(f"\n[Error] Something went wrong: {e}")


if __name__ == "__main__":
    main()