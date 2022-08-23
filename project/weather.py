import requests
from config import weather_api_key
from datetime import datetime, time
from utils import is_time_between, create_icon, format_day

class WeatherAPI:
    def __init__(self):
        self.forecast = []

    def get_data(self):
        response = requests.get(f'http://api.openweathermap.org/data/2.5/forecast?lat=-23.55&lon=-46.64&appid={weather_api_key}&units=metric')
        for item in response.json()['list'][:7]:
            datetime_object = datetime.strptime(item['dt_txt'], "%Y-%m-%d %H:%M:%S")
            day = True if is_time_between(time(6,0), time(18,1), datetime_object.time()) else False
            self.forecast.append({
                'temperature' : (float(item['main']['temp_min']) + float(item['main']['temp_max'])) / 2,
                'icon' : create_icon(item['weather'][0]['id'], day),
                'datetime' : datetime_object
            })

    def create_tweet(self):
        text = f'Previsão do tempo do dia {format_day(self.forecast[0]["datetime"].date())}\n'
        for data in self.forecast:
            text += f'{data["datetime"].time().strftime("%H")}h - {data["icon"]} {data["temperature"] :.0f}°C \n'

        return text