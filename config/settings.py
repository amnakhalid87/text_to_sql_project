from dotenv import load_dotenv
import os

load_dotenv()

AIVEN_DATABASE_URL = os.getenv('AIVEN_DATABASE_URL')
HF_TOKEN = os.getenv('HF_TOKEN')
HF_MODEL = os.getenv('HF_MODEL')
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')   
GROQ_API_KEY=os.getenv('GROQ_API_KEY')