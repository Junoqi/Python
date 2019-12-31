import sys
import requests
import math

api_adress = 'http://api.openweathermap.org/data/2.5/weather?appid=9aac93c4442484af028d88eb1727111c&q='
city = input('Location :')
print()

url = api_adress + city

json_data = requests.get(url).json()
weather = json_data['weather'][0]['main']
temp = json_data['main']['temp']
real_feel = json_data['main']['feels_like']
humidity = json_data['main']['humidity']
temp_min = json_data['main']['temp_min']
temp_max = json_data['main']['temp_max']
air_pressure = json_data['main']['pressure']
wind_speed = json_data['wind']['speed']
final_tempmax = temp_max * 9 / 5 -459.67
final_tempmin = temp_min * 9 / 5 -459.67
final_temp = temp * 9 / 5 -459.67
print('The forecast is ' + weather)
print()
print('The temperature is:')
print(int(final_temp))
print('But it feels like: ')
print(int(real_feel * 9 / 5 -459.67))
print()
print('The humidity is:')
print(humidity)
print()

if weather == 'Thunderstorm':
    print('Stay inside, heavy rain is incoming')
elif weather == 'Rain':
    print('You might want to grab an umbrella!')
elif weather == 'Clear':
    print('Its a clear day outside')
elif weather == 'Drizzle':
    print('Its just a drizzle, maybe bring an umbrella')
elif weather == 'Snow':
    print('Its snowing out! Hope for a snow day!')
elif weather == 'Mist':
    print('A light mist, be careful driving')
elif weather == 'Fog':
    print('Its very foggy out, be careful driving!')
elif weather == 'Tornado':
    print('TORNADO!! FOLLOW STANDARD TORNADO PROCEDURE!!')
elif weather == 'Clouds':
    print('Cloudy out')
    
print()
if final_temp < 30:
    print('Due to the below freezing temperature, you should probaby wear winter gear and limit time outside')
elif final_temp > 90:
    print('Due to the extreme heat, you should limit time in the sun')
print()

more_info = input('Would you like any more specific info? Ex. Sunrise/Sunset:')

if more_info == 'no':
    print('ok')
elif more_info == 'yes':
    print()
    print('Options: Temp min/max, air pressure, wind speed')
    print('Make sure that ONLY the FIRST letter of your response is capital')
    print()  
    options = input('What would you like?: ')
    if options == 'Temp min':
        print(int(final_tempmin))
    elif options == 'Wind speed':
        print(wind_speed)
        print('*Wind speed is measured in MPH (Miles per hour)*')
        print()
    elif options == 'Temp max':
        print(int(final_tempmax))
    elif options == 'Air pressure':
        print(air_pressure)
        print('*Air pressure is measured in atm (Atmospheric Pressure)*')
        print()
    else:
        print('Invalid response')
print('Go to ' + url + ' for more info')
