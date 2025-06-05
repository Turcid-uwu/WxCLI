This is a very simple python script to fetch current watches and warnings for a particular area using the api.weather.gov api

I haven't written python in awhile so this was a fun way to get back into python while integrating my rekindled love of weather!
This also marks the first time I have used an API, and the first time I have managed to work with JSON!

*****************************************************************

USAGE: WxCLI [Your NWS forcast office] [Your state]

ex: WxCLI "NWS Fort Worth TX" TX

*****************************************************************

BUILDING

Use pyinstaller for building
Only dependency is requests, everything else is standard python libs

pyinstaller --name WxCLI -F -c /path/to/main.py
