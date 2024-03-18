import datetime
import Config as c

class TankComponent:
    def __init__(self, proxy):
        self.__state = False
        self.__proxy = proxy

    def getState(self):
        return self.__state
    
    def setState(self, state):
        self.__state = state

    def __str__(self):
        return "TankComponent"
    
    def getProxy(self):
        return self.__proxy
    
    # evt nicht nötig:

   # def writeLog(self, text):
    #    with open("log.txt", "a") as file:
     #       file.write(f"{datetime.datetime.now()}{text}\n")
        