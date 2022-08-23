def is_time_between(startTime, endTime, nowTime): 
    if startTime < endTime: 
        return nowTime >= startTime and nowTime <= endTime 
    else: 
        #Over midnight: 
        return nowTime >= startTime or nowTime <= endTime

# https://openweathermap.org/weather-conditions
def create_icon(id, day):
        # Thunderstorm
        if 200 <= id <= 232:
            return '🌩️'
        # Drizzle/ Rain
        elif 300 <= id <= 531:
            return '🌧️'
        # Snow
        elif 600 <= id <= 622:
            return '❄️'
        # Atmosphere
        elif 701 <= id <= 781:
            return '🌫️'
        # Clear Sky (day/night)
        elif id == 800:
            if day: return '☀️'
            return '🌙'
        # Few Clouds day
        elif id == 801 and day:
            return '🌤️'
        # Scattered Clouds day 
        elif id == 802 and day:
            return '⛅'
        # Broken Clouds day
        elif id == 803 and day:
            return '🌥️'
        # Overcast Clouds or Clouds night
        else:
            return '☁️'

def format_day(date_object):
    months_name = {'01' : 'Janeiro',
        '02' : 'Fevereiro',
        '03' : 'Março',
        '04' : 'Abril',
        '05' : 'Maio',
        '06' : 'Junho',
        '07' : 'Julho',            
        '08' : 'Agosto',    
        '09' : 'Setembro',
        '10' : 'Outubro',
        '11' : 'Novembro',
        '12' : 'Dezembro'
    }
    return f'{date_object.strftime("%d")} de {months_name[date_object.strftime("%m")]} de {date_object.strftime("%Y")}'