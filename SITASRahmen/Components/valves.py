from Components import TankComponent as t

class Ventil(t.TankComponent):  
    def __init__(self, position, proxy):
        super().__init__(proxy)
        self.__position = position
    
    def setPosition(self, position):
        self.__position = position

    def getPosition(self, position):
        return self.__position    
    
    def setState(self, state):
        super().setState(state)
        super().getProxy().forward(self, state)
        self.writeLog()

    def writeLog(self):
        text = "Im a valve"
        super().writeLog(text)