import os
from dotenv import load_dotenv

load_dotenv()

COINPAPRIKA_API_KEY = os.getenv("COINPAPRIKA_API_KEY")
DATABASE_URL = os.getenv("DATABASE_URL")
