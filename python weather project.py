import requests

city_name = 'Canada'
api_key = '198e7338a53f31b3f8c4636eb62038f3'
url = f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric'

response = requests.get(url) # sending get request to the URL
if response.status_code == 200:
  data = response.json()
  print('weather is' ,data['weather'][0]['description'])
  print('current temperature is', data['main']['temp'])
  print('feels like', data['main']['feels_like'])
  print('humidity is ', data['main']['humidity'])