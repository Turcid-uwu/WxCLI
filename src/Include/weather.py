
#Constants

# use api.weather.gov/alerts/active?area={your state} for state wide
# use api.weather.gov/alerts/active/zone/{your NWS county code} for county wide alerts

URL = "https://api.weather.gov/alerts/active?area=TX" #api endpoint for active weather alerts

NWS_OFFICE = "NWS Fort Worth TX" # Local forcast office, make sure this is set to your forcast office

HEADERS = "" # Custom headers, If you want them 

#Classes

class WxAlert: #Using a class will make extending functionality easier later
    def __init__(self, event, area, desc):
        self.event = event
        self.area = area
        self.desc = desc
        self.mark = 0
        self.setMark()

    def setMark(self): #Assign a mark to the alert to determine importance so the list can be sorted
        if 'Emergency' in self.event and 'Tornado' in self.event:
            self.mark = 10

        elif 'Warning' in self.event and 'Tornado' in self.event:
            self.mark = 9

        elif 'Warning' in self.event and 'Thunderstorm' in self.event:
            self.mark = 8
        
        elif 'Special Weather Statement' in self.event:
            self.mark = 7

        elif 'Warning' in self.event and 'Flood' in self.event:
            self.mark = 6

        elif 'Watch' in self.event and 'Tornado' in self.event:
            self.mark = 5

        elif 'Watch' in self.event and 'Thunderstorm' in self.event:
            self.mark = 4

        elif 'Watch' in self.event and 'Flood' in self.event:
            self.mark = 3


#Functions

def parseAlerts(content): # parse the values we want from the api response
    try:

        test = content['features'][0]['properties']['event'] # Try to access the first element to see if there is any active alerts
        alertList = []

        for alert in content['features']: 

            if alert['properties']['senderName'] == NWS_OFFICE: # Not really needed if going by county/zone, but still helpful to have

                nAlert = WxAlert(alert['properties']['event'], alert['properties']['areaDesc'], alert['properties']['headline']) 
                alertList.append(nAlert)
        
        alertList.sort(key=lambda x: x.mark, reverse=True)
        return alertList

    except IndexError: # If no alerts, an Index error will be raised
        return IndexError
        
