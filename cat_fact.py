from urllib import response
import requests
'''
This program uses an api that calls to the catfact/fact api and returns 
the api data from the catfact/fact api
'''
#had to make an intentional typo because response would crash
try:
    resoponse = requests.get('https://catfact.ninja/fact') #request and responce
    data = resoponse.json()
    fact = data['fact'] #'fact' key in api only 

    while True:
        resoponse.raise_for_status()#exception for 400 or 500
        fact = data['fact']

        new_fact = input('\n' +'press enter for cat fact    ' )
        if new_fact == '':
            print(f'\n {resoponse.status_code}')#200(successful response)
            print(f'\n{fact}\n')#prints value of fact key
            print(f'{resoponse.text}\n')#prints all object data
            data = requests.get('https://catfact.ninja/fact').json()# new response
        else:
            break
except Exception as e:
    print(f'url catfact.ninja/{e} does not exist')

    