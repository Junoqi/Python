import sys
import requests
import math

api_adress = 'http://api.openweathermap.org/data/2.5/weather?appid=9aac93c4442484af028d88eb1727111c&q='
city = input('Location:')
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
lon = json_data['coord']['lon']
lat = json_data['coord']['lat']
country_name_farh = json_data['sys']['country']
final_tempmax = temp_max * 9 / 5 -459.67
final_tempmin = temp_min * 9 / 5 -459.67
final_temp = temp * 9 / 5 -459.67
windspeed_kph = wind_speed * 1.609

fahernheit_countries = {'AT', 'AR', 'KY', 'FM', 'MY', 'US'}

print('The forecast is ' + weather)
print()
print('The temperature is:')

if country_name_farh in fahernheit_countries:
    print(int(final_temp))
else:
    print(int(temp - 273.15))
print('But it feels like: ')

if country_name_farh in fahernheit_countries:
    print(int(real_feel * 9 / 5 -459.67))
else:
    print(int(real_feel - 273.15))
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

more_info = input('Would you like any more specific info? Ex. High temp, low temp:')

if more_info == 'no':
    print('ok')
elif more_info == 'yes':
    print()
    print('Options: Temp min/max, air pressure, wind speed, Lon_Lat')
    print('Make sure that ONLY the FIRST letter of your response is capital')
    print()  
    options = input('What would you like?: ')
    if options == 'Temp min':
        if country_name_farh in fahernheit_countries:
            print(int(final_tempmin))
        else:
            print(int(final_tempmin - 32 * 5 / 9))
    elif options == 'Wind speed':
        if country_name_farh in fahernheit_countries:
            print(wind_speed + 3)
            print('*Wind speed is measured in MPH (Miles per hour)*')
        else:
            print(windspeed_kph + 3)
            print('*Wind speed is measured in KPH (Kilometers per hour)*')
    elif options == 'Temp max':
        if country_name_farh in fahernheit_countries:
            print(int(final_tempmax))
        else:
            print(int(final_tempmax - 32 * 5 / 9))
    elif options == 'Air pressure':
        print(air_pressure)
        print('*Air pressure is measured in atm (Atmospheric Pressure)*')
        print()
    elif options == 'Lon_lat':
        print('Longitude:')
        print(lon)
        print('Latitude:')
        print(lat)
        print()
    else:
        print('INVALID RESPONSE')
print('Go to ' + url + ' for more info')
