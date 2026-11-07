
# gemini_assistant.py

# Import the Gemini package.
from google import genai

# Import the function that reads our .env file.
from dotenv import load_dotenv

# Import os to access environment variables.
import os


# Find the folder containing this Python file.
BASE_FOLDER = os.path.dirname(os.path.abspath(__file__))

# Build the exact location of the .env file.
ENV_FILE = os.path.join(BASE_FOLDER, "smp.env")

# Load the environment variables from that file.
load_dotenv(dotenv_path=ENV_FILE, override=True)

# Read the Gemini API key.
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Check whether an API key was provided.
if not GEMINI_API_KEY:
    raise ValueError(
        "Gemini API key not found. "
        "Please check your .env file."
    )


# Create a Gemini client.
client = genai.Client(api_key=GEMINI_API_KEY)


# Ask Gemini a question and receive an answer.
def ask_gemini(question):

    try:
        # Send the question to Gemini.
        response = client.models.generate_content(
            model="gemini-3.5-flash-lite",
            contents=question
        )
       

        # Return Gemini's answer.
        return response.text

    except Exception as error:

        # Display the error in the terminal.
        print("Gemini error:", error)

        return "Sorry, I could not get an answer from Gemini."

    
