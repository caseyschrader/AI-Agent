import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

def main():
    load_dotenv()

    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    args = sys.argv[1:]

    if not args:
        print("Please enter a prompt")
        print('Example: python main.py "Enter your prompt here"')
        sys.exit(1)
    user_prompt = " ".join(args)

    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    if "--verbose" in user_prompt:
        generate_verbose_content(client, messages, user_prompt)

    generate_content(client, messages)

def generate_content(client, messages):
    response = client.models.generate_content(
        model='gemini-2.5-flash', 
        contents=messages
    )
    print(f"Reponse: {response.text}")


def generate_verbose_content(client, messages, user_prompt):
    response = client.models.generate_content(
        model='gemini-2.5-flash', 
        contents=messages
    )
    print(f"User prompt: {user_prompt}")
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    print(f"\nReponse: {response.text}")

if __name__ == "__main__":
    main()
