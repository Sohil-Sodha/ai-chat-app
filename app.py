def main():
    print("Welcome to the AI Chat App!")
    print("Project foundation successfully set up. 🎉")

if __name__ == "__main__":
    main()

from gemini import GeminiClient

ai = GeminiClient()

pmt = input("Enter your prompt: ")
res = ai.generate_response(pmt)

print(res)