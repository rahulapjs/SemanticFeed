import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.environ["DATABASE_URL"]
GOOGLE_API_KEY = os.environ["GOOGLE_API_KEY"]
