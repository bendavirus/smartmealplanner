
# check_env.py

import os
from dotenv import load_dotenv

# Find the project folder.
folder = os.path.dirname(os.path.abspath(__file__))

# Find the .env file.
env_file = os.path.join(folder, "smp.env")

# Check whether the file exists.
print("Does smp.env exist?", os.path.exists(env_file))

# Load the environment file.
load_dotenv(dotenv_path=env_file, override=True)

# Check whether the API key was found.
api_key = os.getenv("GEMINI_API_KEY")

if api_key:
    print("API key found: YES")
else:
    print("API key found: NO")

# Display the file location, not the API key.
print("Environment file location:", env_file)
