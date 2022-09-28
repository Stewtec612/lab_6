import requests
from pprint import pprint
import os
'''
This program collects the users input for 
    -pick a city in a state from usa
    -pick a city from a different country
a dictionary collects user inputs and replaces the url query
returns all weather info for that location 
'''

key = os.environ.get('WEATHER_KEY')
print(key)
#TODO weather description, and 
# wind speed for every three hour interval,over the next 5 days.
def main():
    us_or_other = input('usa or other?')

    if us_or_other == 'usa':
        city = input('Enter name of city: ')
        state = input('Enter state initials: ')
        country = 'us'
        location = f'{city},{state},{country}'
        query = {'q': {location},'units':'imperial','appid': key}
        print(f'\n FORCAST FOR {city.upper()}, {state.upper()},{country.upper()}\n')

    elif us_or_other == 'other':
        city = input('Enter name of city: ')
        country = input("enter country\'s initials: ")
        location = f'{city},{country}'
        query = {'q': {location},'units':'imperial','appid': key}
        print(f'\n FORCAST FOR {city.upper()}, {country.upper()}\n')

    weather_url = f'https://api.openweathermap.org/data/2.5/weather?'
    data = requests.get(weather_url,params=query).json()
    weather_description = data['weather'][0]['description']
    temp = data['main']['temp']
    windspeed = data ['wind']['speed']

    #pprint(data)
    
    print(f'Forcast: {weather_description}\n Temprature: {temp}F \n Windspeed: {windspeed} MPH')

main()