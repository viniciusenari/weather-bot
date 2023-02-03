import os
from dotenv import load_dotenv
load_dotenv()

auth_multi = os.getenv("AUTH_MULTI")
auth_token = os.getenv("AUTH_TOKEN")
personalization_id = os.getenv("PERSONALIZATION_ID")
twid = os.getenv("TWID")
bearer = os.getenv("BEARER")
csrf_token = os.getenv("CSRF_TOKEN")

weather_api_key = os.getenv("WEATHER_API_KEY")