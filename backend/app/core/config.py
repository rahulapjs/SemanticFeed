import os
from dotenv import load_dotenv

load_dotenv()

# Google API Key
GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY")

# Database Configuration
# Allow setting full DATABASE_URL or constructing it from parts
DATABASE_URL = os.environ.get("DATABASE_URL")

if not DATABASE_URL:
    POSTGRES_USER = os.environ.get("POSTGRES_USER", "user")
    POSTGRES_PASSWORD = os.environ.get("POSTGRES_PASSWORD", "password")
    POSTGRES_SERVER = os.environ.get("POSTGRES_SERVER", "localhost")
    POSTGRES_PORT = os.environ.get("POSTGRES_PORT", "5432")
    POSTGRES_DB = os.environ.get("POSTGRES_DB", "semanticdb")
    
    DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"
