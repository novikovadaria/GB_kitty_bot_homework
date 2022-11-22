from datetime import datetime
import requests
API_weather = '504ae7a2597100bebb0b96ec3e727072'


def get_weather(city):
    req = requests.get(
        f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_weather}&units=metric')
    date = req.json()
    city = date['name']
    current_temp = date['main']['temp']
    speed_of_wind = date['wind']['speed']
    sunrise_time = datetime.fromtimestamp(date['sys']['sunrise'])
    sunset_time = datetime.fromtimestamp(date['sys']['sunset'])

    return f'Погода в городе {city} 🏙.\nТемпература: 🌡 {current_temp}°С .\nСкорость ветра: {speed_of_wind} м/c.\nВремя восхода солнца: 🌅 {sunrise_time}.\nВремя заката: 🌇 {sunset_time}.\nХорошего дня! 😸'
