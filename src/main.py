#This is a program that will fetch the current watches and warnings from api.weather.gov for a given area
import requests
import json
from time import sleep
import os
from Include.weather import *
from Include.parse import *

def main():

    # Get OS name
    osName = os.name
    if osName == 'posix':
        CLEARCMD = 'clear'
    else:
        CLEARCMD = 'cls'
  
    while True:
        os.system(CLEARCMD)
        req = requests.get(URL, headers=HEADERS)
        rawResponse = json.loads(req.content)
        alerts = parseAlerts(rawResponse)

        if alerts != IndexError:

            print('*---------------------------------------------------*')
            for alert in alerts:
                print(alert.event)
                print(alert.area)
                print(alert.desc)
                print('\n')
                sleep(2)
            print('*---------------------------------------------------*')
            sleep(60)
            os.system(CLEARCMD)

        else:
            print('No Alerts for your area are currently issued')
            sleep(60)
            os.system(CLEARCMD)

if __name__ == '__main__':
    main()
