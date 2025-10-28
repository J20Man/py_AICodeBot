import os
import sys
from config import SYSTEM_PROMPT
from dotenv import load_dotenv
from google import genai
from google.genai import types
from functions.get_files_info import available_functions, get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python_file import run_python_file


def main():
    load_dotenv()
    verbose = "--verbose" in sys.argv
    args = []
    for arg in sys.argv[1:]:
        if not arg.startswith("--"):
            args.append(arg)
    
    if not args:
        print("AI Code Assistant")
        print('\nUsage: python main.py "your prompt here" [--verbose]')
        sys.exit(1)

    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    user_prompt = " ".join(args)

    if verbose:
        print(f"User prompt: {user_prompt}\n")

    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
        ]
    
    generate_content(client, messages, verbose)

        
def generate_content(client, messages, verbose):
    if len(sys.argv) > 1: 
        response = client.models.generate_content(
            model='gemini-2.0-flash-001', 
            contents=messages,
            config=types.GenerateContentConfig(
                tools=[available_functions], 
                system_instruction=SYSTEM_PROMPT
            ),
        )

        generated_text = ""
        
        try:
            if not response.function_calls:
                generated_text = response.candidates[0].content[0].text
            if response.function_calls:
                for call in response.function_calls:

                    if call.name == "get_files_info":
                        func = {
                            call.name: call.args
                        }
                        print(f"Calling function: {func}")

                    elif call.name == "get_file_content":
                        # filename = call.args.get("filename")
                        # result = get_file_content(os.getcwd(), filename)
                        # print(result)
                        func = {
                            call.name: call.args
                        }
                        print(f"Calling function: {func}")

                    elif call.name == "write_file":
                        # filename = call.args.get("filename")
                        # contents = call.args.get("contents")
                        # result = write_file(os.getcwd(), filename, contents)
                        # print(result)
                        func = {
                            call.name: call.args
                        }
                        print(f"Calling function: {func}")

                    elif call.name == "run_python_file":
                        # filename = call.args.get("filename")
                        # result = run_python_file(os.getcwd(), filename)
                        # print(result)
                        func = {
                            call.name: call.args
                        }
                        print(f"Calling function: {func}")

                    else:
                        print(f"Unknown function call: {call.name}")

        except Exception:
            generated_text = response.text

        print(generated_text)

        if verbose:
            response_tokens = response.usage_metadata.candidates_token_count
            prompt_tokens = response.usage_metadata.prompt_token_count
            print(f"User prompt: {response.text} \n Prompt tokens: {prompt_tokens} \n Response tokens: {response_tokens}")
        
    else:
        print("Please provide a prompt as a command-line argument.")
        sys.exit(1)

if __name__ == "__main__":
    main()
