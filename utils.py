# utils.py — Reusable UI helper functions for the AI Chat App.

def print_banner() -> None:
    # Prints the welcome banner at application startup.

    print("=" * 40)
    print("        Welcome to AI Chat App!")
    print("   Type 'exit' or 'quit' to leave.")
    print("=" * 40)

def formate_ai_response(text: str) -> str:
    
    separator = "-" * 40
    return f"\n{separator}\nAI: {text}\n{separator}"

def print_goodbye() -> None:
    print("\nGoodbye! Thanks for chatting. 👋")