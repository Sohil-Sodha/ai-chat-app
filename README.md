# AI Chat App

A beginner-friendly, production-quality CLI chat application powered by Google's Gemini API.
Built incrementally with a clean, layered architecture that separates configuration, business logic, API communication, and presentation into focused, single-responsibility modules.

---

## Features

- Conversational AI powered by Google Gemini
- Persistent conversation memory within a session
- System prompt integration for consistent AI behaviour
- Clean, layered architecture (CLI → Business Logic → API Service)
- Centralised prompt management
- Graceful error handling (invalid API key, network issues, empty input)
- Friendly CLI interface with formatted output

---

## Folder Structure

```
ai-chat-app/
│
├── app.py            # Entry point — CLI loop and user interaction
├── chat.py           # Business logic — ChatService and ChatSession
├── gemini.py         # Gemini API service layer — GeminiClient
├── config.py         # Configuration — loads and validates environment variables
├── prompts.py        # Prompt management — system prompts and prompt builders
├── utils.py          # UI helpers — banner, formatting, goodbye message
├── requirements.txt  # Project dependencies
├── .env              # Environment variables (never commit this file)
├── .gitignore        # Files excluded from version control
└── README.md         # Project documentation
```

---

## Tech Stack

| Component       | Technology                        |
|-----------------|-----------------------------------|
| Language        | Python 3.10+                      |
| AI Model        | Google Gemini 2.5 Flash           |
| AI SDK          | `google-genai`             |
| Config Loading  | `python-dotenv`                   |
| Interface       | CLI (built-in `input` / `print`)  |

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/Sohil-Sodha/ai-chat-app.git
cd ai-chat-app
```

### 2. Create and activate a virtual environment

**macOS / Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## Configuration

### 1. Get a Gemini API key

Visit [Google AI Studio](https://aistudio.google.com/app/apikey) and generate a free API key.

### 2. Create a `.env` file in the project root

```
GEMINI_API_KEY=your_api_key_here
```

> ⚠️ Never commit your `.env` file. It is already listed in `.gitignore`.

---

## Running the App

```bash
python app.py
```

---

## Example Conversation

```
========================================
        Welcome to AI Chat App!
   Type 'exit' or 'quit' to leave.
========================================

You: What is the capital of Japan?
----------------------------------------
AI: The capital of Japan is Tokyo.
----------------------------------------

You: How large is its population?
----------------------------------------
AI: Tokyo is one of the most populous cities in the world,
with a greater metropolitan population of around 37 million people.
----------------------------------------

You: exit

Goodbye! Thanks for chatting. 👋
```

---

## Dependencies

Listed in `requirements.txt`:

```
google-genai
python-dotenv
```

Install them with:

```bash
pip install -r requirements.txt
```

---

## Architecture Overview

The project is organised into distinct layers, each with a single responsibility:

| File          | Responsibility                                        |
|---------------|-------------------------------------------------------|
| `app.py`      | Runs the CLI loop; handles all user input and output  |
| `chat.py`     | Manages conversation flow and session history         |
| `gemini.py`   | Communicates with the Gemini API                      |
| `config.py`   | Loads and validates the API key from `.env`           |
| `prompts.py`  | Stores and builds system prompts                      |
| `utils.py`    | Provides reusable UI formatting helpers               |

Data flows in one direction:

```
app.py → ChatService → GeminiClient → Gemini API
```

---

## License

This project is intended for learning purposes and is not licensed for production use.
