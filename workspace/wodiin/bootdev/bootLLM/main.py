import os
import sys
from dotenv import load_dotenv
from google import genai
import argparse
from google.genai import types
import prompts
from functions.available_functions import available_functions
from functions.call_function import call_function

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

    for _ in range(20):
        response, list_of_function_response = generate_content(client, messages, args.verbose, args.user_prompt)

        for candidate in response.candidates:
            messages.append(candidate.content)
        
        
        if response.function_calls is None:
            break

        messages.append(types.Content(role="user", parts=list_of_function_response))
    else: 
        print("Reached maximum number of iterations.")
        sys.exit(1)

    
    

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
    
    list_of_function_response = []
    # Print the generated content
    if response.function_calls is not None:
        for function_call in response.function_calls:
            function_call_result = call_function(function_call, verbose)
            if function_call_result.parts == None:
                raise RuntimeError("Function call did not return any parts.")
            if function_call_result.parts[0].function_response == None:
                raise RuntimeError("Function call did not return a function response.")
            if function_call_result.parts[0].function_response.response == None:
                raise RuntimeError("Function call did not return a response.")
            list_of_function_response.append(function_call_result.parts[0])
            if verbose:
                print(f"-> {function_call_result.parts[0].function_response.response}")
                
    else:
        print(response.text)

    return response, list_of_function_response

if __name__ == "__main__":
    main()
