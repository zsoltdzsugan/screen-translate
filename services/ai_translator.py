import os
import json
import requests
import logging

# Load environment variables (you can replace this with dotenv or manually load)
from dotenv import load_dotenv
load_dotenv()  # Load the .env file

def get_translation(text):
    # Get the API key from the environment variable
    api_key = os.getenv("OPENAI_API_KEY") or os.getenv("OPENAI_API_KEY_FALLBACK")
    
    if not api_key:
        logging.error("OpenAI API key is missing.")
        return "Error: Missing API key"
    
    # Prepare request data
    request_data = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {
                "role": "user",
                "content": f"You are a helpful professional Hungarian-English translator. Translate the following, text to Hungarian: {text}"
            }
        ]
    }

    # Set up headers and endpoint
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    try:
        # Send POST request to OpenAI API
        response = requests.post(url, headers=headers, data=json.dumps(request_data))
        
        # Check for successful response
        if response.status_code != 200:
            logging.error(f"API error: {response.text}")
            return f"Error: API returned status {response.status_code}"
        
        # Parse the JSON response
        response_data = response.json()
        
        # Extract translated text from the response
        choices = response_data.get("choices", [])
        if not choices:
            logging.error("No choices found in response.")
            return "Error: No translation found"

        message = choices[0].get("message", {})
        translated_text = message.get("content", "").strip()
        
        if not translated_text:
            logging.error("Translation not found in response.")
            return "Error: Translation not found"
        
        return translated_text
    
    except Exception as e:
        logging.error(f"Error: {e}")
        return "Error occurred during translation"

