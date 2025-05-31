#This is a program that will fetch the current watches and warnings from api.weather.gov for a given area
import requests
import json
from time import sleep
import os
from Include.weather import *

def main():
  
    while True:
        os.system('clear')
        req = requests.get(URL)
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
            os.system('clear')

        else:
            print('No Alerts for your area are currently issued')
            sleep(60)
            os.system('clear')

if __name__ == '__main__':
    main()
