from dotenv import load_dotenv
import os

# Load the environment variables from the .env file
load_dotenv('openai_key.env')

# Get the OpenAI API key from the environment variables
api_key = os.getenv("OPENAI_API_KEY")

# Optionally, set it as an environment variable if needed for further use
os.environ["OPENAI_API_KEY"] = api_key

