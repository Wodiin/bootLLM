import os
from dotenv import load_dotenv
from google import genai
import argparse
from google.genai import types
import prompts
from functions.call_functions import available_functions

def main():


    # Set up command-line argument parsing 
    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()


    # Load environment variables from the .env file
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    if api_key is None:
        raise RuntimeError("GEMINI_API_KEY is not set in the environment variables.")
    
    # Initialize the Gemini API client
    client = genai.Client(api_key=api_key)
    
    # Create a message with the user's prompt
    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]

    # Generate content using the Gemini API and print the results
    generate_content(client, messages, args.verbose, args.user_prompt)
    

def generate_content(client, messages, verbose, user_prompt):

    # Generate content using the Gemini API
    response = client.models.generate_content(model="gemini-2.5-flash", contents=messages, config=types.GenerateContentConfig(tools=[available_functions], system_instruction=prompts.system_prompt, temperature=0))
    
    # Check if the response contains usage metadata and print token counts
    if response.usage_metadata != None:
        pass
    else:
        raise RuntimeError("Failed API Request") 
    
    # If verbose mode is enabled, print the user prompt and token counts
    if verbose:
        print(f"User prompt: {user_prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    

    # Print the generated content
    if response.function_calls is not None:
        for function_call in response.function_calls:
            print(f"Calling function: {function_call.name}({function_call.args})")
    else:
        print(response.text)

if __name__ == "__main__":
    main()
