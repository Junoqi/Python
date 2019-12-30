import requests

api_adress = 'http://api.openweathermap.org/data/2.5/weather?appid=9aac93c4442484af028d88eb1727111c&q='
city = input('City Name :')
print()

url = api_adress + city

json_data = requests.get(url).json()
weather = json_data['weather'][0]['main']
print(weather)
print()

if weather == 'Thunderstorm':
    print('Stay inside, heavy rain is incoming')
elif weather == 'Rain':
    print('You might want to grab an umbrella!')
    
print()    
print('Go to ' + url + ' for more info')