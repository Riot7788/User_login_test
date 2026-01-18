import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("BASE_URL")

STANDARD_USER = os.getenv("STANDARD_USER")
STANDARD_PASSWORD = os.getenv("STANDARD_PASSWORD")

LOCKED_USER = os.getenv("LOCKED_USER")
PERFORMANCE_USER = os.getenv("PERFORMANCE_USER")

WRONG_PASSWORD = os.getenv("WRONG_PASSWORD")
