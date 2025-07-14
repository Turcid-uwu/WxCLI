#Classes

class WxAlert: #Using a class will make extending functionality easier later
    def __init__(self, event, area, desc):
        self.event = event
        self.area = area
        self.desc = desc
        self.mark = 0
        self.setMark()

    def setMark(self): #Assign a mark to the alert to determine importance so the list can be sorted
        if 'Tornando Emergency' in self.event:
            self.mark = 10

        elif 'Tornado Warning' in self.event:
            self.mark = 9

        elif 'Thunderstorm Warning' in self.event:
            self.mark = 8
        
        elif 'Special Weather Statement' in self.event:
            self.mark = 7

        elif 'Flood Warning' in self.event:
            self.mark = 6

        elif 'Tornando Watch' in self.event:
            self.mark = 5

        elif 'Thunderstorm Watch' in self.event:
            self.mark = 4

        elif 'Flood Watch' in self.event:
            self.mark = 3

