    
from google import genai
import os
from app.core.config import GOOGLE_API_KEY

def get_client():
    return genai.Client(
        api_key=GOOGLE_API_KEY
    )
