#This is a program that will fetch the current watches and warnings from api.weather.gov for a given area
import requests
import json
from time import sleep
import os
from Include.weather import *
from Include.parse import *
import argparse

def main(url, nws):
    HEADERS = {'user-agent': 'WxCLI-0.0.2 | turicd@protonmail.com'} # Custom headers, for identifcation!

    # Get OS name
    osName = os.name

    if osName == 'posix':
        CLEARCMD = 'clear'
    else:
        CLEARCMD = 'cls'
  
    while True:
        os.system(CLEARCMD)
        req = requests.get(url, headers=HEADERS)
        rawResponse = json.loads(req.content)
        alerts = parseAlerts(rawResponse, nws)

        if alerts != IndexError:

            print('*---------------------------------------------------*', end='')
            print('\n')
            for alert in alerts:
                print(alert.event)
                print(alert.area)
                print(alert.desc)
                print('\n', end='')
                sleep(2)
            print('*---------------------------------------------------*')
            sleep(60)
            os.system(CLEARCMD)

        else:
            print('No Alerts for your area are currently issued')
            sleep(60)
            os.system(CLEARCMD)

def setup(args): # Setup vars form given args
    URL = "https://api.weather.gov/alerts/active?area=" + args.NWS_STATION[-2:] #api endpoint for active weather alerts
    NWS_OFFICE = args.NWS_STATION # Local forcast office, make sure this is set to your forcast office
    main(URL, NWS_OFFICE)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='WxCLI', description='A command line app that pulls the current watches in a given area.')
    parser.add_argument('NWS_STATION', help='Full name of the desired NWS forcast station')
    args = parser.parse_args()
    setup(args)
