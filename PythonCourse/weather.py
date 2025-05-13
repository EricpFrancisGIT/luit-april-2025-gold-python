
import requests

url = "https://api.open-meteo.com/v1/forecast"
response = requests.get(url)
weather_json = response.json()
print(weather_json)