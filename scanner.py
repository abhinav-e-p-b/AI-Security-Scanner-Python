import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables from .env file
load_dotenv()

# Configure with your API key from environment variable
api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=api_key)

# Initialize the model
model = genai.GenerativeModel("gemini-2.5-flash")

# ============================================================
# YOUR CODE GOES BELOW HERE
# ============================================================

# Test with a simple prompt
response = model.generate_content("Say 'Hello, security scanner!' if you can hear me.")

print(response.text)

# ============================================================
# YOUR CODE GOES ABOVE HERE
# ============================================================
