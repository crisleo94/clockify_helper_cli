from dotenv import load_dotenv
import os

load_dotenv()

API_URL = 'https://api.clockify.me/api/v1'
API_KEY = os.getenv('API_KEY')