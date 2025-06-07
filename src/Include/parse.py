from Include.weather import *

def parseAlerts(content, nws): # parse the values we want from the api response

    try:

        test = content['features'][0]['properties']['event'] # Try to access the first element to see if there is any active alerts
        alertList = []

        for alert in content['features']: 

            if alert['properties']['senderName'] == nws: # Not really needed if going by county/zone, but still helpful to have

                nAlert = WxAlert(alert['properties']['event'], alert['properties']['areaDesc'], alert['properties']['headline']) 
                alertList.append(nAlert)
        
        if len(alertList) == 0:
            return IndexError #Needed so that if after creating the alert list the no warnings message will show if on alerts are present
        
        else:
            alertList.sort(key=lambda x: x.mark, reverse=True)
            return alertList

    except IndexError: # If no alerts, an Index error will be raised
        return IndexError
        