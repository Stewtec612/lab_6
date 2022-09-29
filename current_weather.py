from webbrowser import get
import requests
from pprint import pprint
import os
from datetime import datetime
'''
This program collects the users input for 
    -pick a city in a state from usa
    -pick a city from a different country
a dictionary collects user inputs and replaces the url query
returns all weather info for that location 
'''

key = os.environ.get('WEATHER_KEY')
#print(key)
#TODO weather description, and 
# wind speed for every three hour interval,over the next 5 days.

def main():
    print('*---Daily Weather Forcast--*')
    us_or_other = input('usa or other?')

    if us_or_other == 'usa':
        city = input('Enter name of city: ')
        state = input('Enter state initials: ')
        country = 'us'
        location = f'{city},{state},{country}'
        query = {'q': {location},'units':'imperial','appid': key}
        print(f'\n FORCAST FOR {city.upper()}, {state.upper()},{country.upper()}\n')
        #get_usa_weather()
        


    elif us_or_other == 'other':
        city = input('Enter name of city: ')
        country = input("enter country\'s initials: ")
        location = f'{city},{country}'
        query = {'q': {location},'units':'imperial','appid': key}
        print(f'\n FORCAST FOR {city.upper()}, {country.upper()}\n')

    data = get_current_weather_response(query)
    display_forcast(data)
    

    #pprint(data)
    
    

def get_current_weather_response(location_query):
    #weather_url = f'https://api.openweathermap.org/data/2.5/weather?'
    forcast_5_url = 'http://api.openweathermap.org/data/2.5/forecast?'
    data = requests.get(forcast_5_url,params=location_query).json()
    return data 

def display_forcast(data):
    #pprint(data)
    list_of_forcasts  = data['list']
    for forcast in (list_of_forcasts):
        timestamp = forcast['dt']
        forcast_date = datetime.fromtimestamp(timestamp)
        weather_description = forcast['weather'][0]['description']
        windspeed = forcast['wind']['speed']
        temp = forcast['main']['temp']
        forcast_day = forcast_date.day
        forcast_month = forcast_date.month
        forcast_year = forcast_date.year
        

        for i in range (len(list_of_forcasts)):
            print(forcast_date.strftime('%b') + ' ' + forcast_date.strftime('%d') + ', ' + forcast_date.strftime('%Y')) 
            i += 1
            print('Time: ' + forcast_date.strftime('%I') + ':' + forcast_date.strftime('%M' + ' ' + forcast_date.strftime('%p')))
            print(f' Forcast: {weather_description}\n Temprature: {temp}F \n Windspeed: {windspeed} MPH\n')
        
            



    
    
    


def get_usa_weather(city, state):
    city = input('Enter name of city: ')
    state = input('Enter state initials: ')
    country = 'us'
    location = f'{city},{state},{country}'
    query = {'q': {location},'units':'imperial','appid': key}

    return query

main()
