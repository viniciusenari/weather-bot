import os
from dotenv import load_dotenv
load_dotenv()

twitter_api_key = os.getenv("API_KEY")
twitter_api_key_secret = os.getenv("API_KEY_SECRET")
twitter_access_token = os.getenv("ACCESS_TOKEN")
twitter_access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")
weather_api_key = os.getenv("WEATHER_API_KEY")