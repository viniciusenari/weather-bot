from json import load
import requests
import os
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("WEATHER_API_KEY")

response = requests.get(f'http://api.openweathermap.org/data/2.5/forecast?lat=-23.55&lon=-46.64&appid={api_key}')
print(response.json())

for item in response.json()['list']:
    print(item)