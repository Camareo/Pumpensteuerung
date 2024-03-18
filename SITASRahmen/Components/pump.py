
from Components import TankComponent as t

class Pump(t.TankComponent):
    def __init__(self, position, proxy):
        super().__init__(proxy)
        self.__position = position
    
    def setPosition(self, position):
        self.__position = position  

    def getPosition(self, position):
        return self.__position

    def setState(self, state):  # setzt Zustand und leitet ihn an Proxy weiter der Lampe
        super().setState(state)
        super().getProxy().forward(self, state)    

    def writeLog(self):
        text = "I'm a pump"
        super().writeLog(text)