# prompts.py — Centralised prompt management for the AI Chat App.

# ---------------------------------------------------------------------------
# System Prompts
# Fixed instructions that define the AI's personality and behaviour.
# These are sent once to set the context before any user message.
# ---------------------------------------------------------------------------

DEFAULT_SYSTEM_PROMPT: str = (
    "You are a helpful, friendly, and concise AI assistant. "
    "Answer clearly and honestly. "
    "If you do not know something, say so rather than guessing."
)

CONCISE_SYSTEM_PROMPT: str = (
    "You are a concise AI assistant. "
    "Always reply in three sentences or fewer."
)

FORMAL_SYSTEM_PROMPT: str = (
    "You are a professional AI assistant. "
    "Use formal language and avoid casual phrasing."
)

# ---------------------------------------------------------------------------
# Dynamic Prompt Builders
# Functions that construct prompts requiring runtime values.
# ---------------------------------------------------------------------------

def build_system_prompt(personality: str, extra_instructions: str = "") -> str:
    # Builds a custom system prompt at runtime.

    base = f"You are {personality}."

    if extra_instructions:
        return f"{base} {extra_instructions}"
    
    return base

def buiild_context_prompt(context: str, user_message: str) -> str:
    # Wraps a user message with additional background context.
    # Useful when the AI needs reference material before answering.

    return (
        f"Use the following context to help answer the question.\n\n"
        f"Context:\n{context}\n\n"
        f"Question:\n{user_message}"
    )