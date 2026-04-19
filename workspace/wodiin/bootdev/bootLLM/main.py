import os
from dotenv import load_dotenv
from google import genai

# Load environment variables from the .env file
load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
if api_key is None:
    raise RuntimeError("GEMINI_API_KEY is not set in the environment variables.")

# Initialize the Gemini API client
client = genai.Client(api_key=api_key)

# Generate content using the Gemini API
response = client.models.generate_content(model="gemini-2.5-flash", contents="Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum.")

# Check if the response contains usage metadata and print token counts
if response.usage_metadata != None:
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
else:
    raise RuntimeError("Failed API Request") 

# Print the generated content
print(response.text)


def main():
    print("Hello from bootllm!")


if __name__ == "__main__":
    main()
