import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("SUNO_API_KEY")

print(f"API Key cargada: {API_KEY}") 
