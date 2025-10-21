import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)


def main():
    
    



    if len(sys.argv) > 1:
        # Gets the User Prompt
        user_prompt = sys.argv[1]
        # Stores the message history
        messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
        ]
        # API Call 
        response = client.models.generate_content(
            model='gemini-2.0-flash-001', 
            contents=messages,
        )
        # Prints the response and token usage
        response_tokens = response.usage_metadata.candidates_token_count
        prompt_tokens = response.usage_metadata.prompt_token_count
        print(f"{response.text} \n Prompt tokens: {prompt_tokens} \n Response tokens: {response_tokens}")
    

        

    else:
        print("Please provide a prompt as a command-line argument.")
        sys.exit(1)
        




if __name__ == "__main__":
    main()
