
# test_gemini.py

# Import our Gemini assistant.
from gemini_assistant import ask_gemini

# Ask Gemini a simple question.
question = "What is Nigerian Jollof Rice?"

# Get Gemini's response.
answer = ask_gemini(question)

# Display the answer.
print("\nGEMINI RESPONSE:")
print(answer)
