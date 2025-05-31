#This is a program that will fetch the current watches and warnings from api.weather.gov for a given area
import requests
import json
from time import sleep
import os

#Constants
URL = "https://api.weather.gov/alerts/active?area=TX" #api endpoint for active weather alerts
# use api.weather.gov/alerts/active?area={your state} for state wide
# use api.weather.gov/alerts/active/zone/{your NWS county code} for county wide alerts

NWS_OFFICE = "NWS Fort Worth TX" # Local forcast office, make sure this is set to your forcast office
HEADERS = "" # Custom headers, If you want them 

class WxAlert: #Using a class will make extending functionality easier later
    def __init__(self, event, area, desc):
        self.event = event
        self.area = area
        self.desc = desc

def parseAlerts(content):
    try:

        test = content['features'][0]['properties']['event'] # Try to access the first element to see if there is any active alerts
        alertList = []

        for alert in content['features']: 

            if alert['properties']['senderName'] == NWS_OFFICE:

                nAlert = WxAlert(alert['properties']['event'], alert['properties']['areaDesc'], alert['properties']['parameters']['NWSheadline'][0]) 
                alertList.append(nAlert)

        return alertList

    except IndexError: # If no alerts, an Index error will be raised
        return IndexError
        

def main():

    while True:

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
