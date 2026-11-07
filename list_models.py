
from google import genai
from dotenv import load_dotenv
import os

# Load the API key from the .env file.
BASE_FOLDER = os.path.dirname(os.path.abspath(__file__))
ENV_FILE = os.path.join(BASE_FOLDER, "smp.env")

load_dotenv(dotenv_path=ENV_FILE)

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("Gemini API key not found!")
else:
    client = genai.Client(api_key=api_key)

    try:
        print("Available Gemini models:\n")

        for model in client.models.list():
            print(model.name)

    except Exception as error:
        print("Error:", error)
