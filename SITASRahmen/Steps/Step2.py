# -*- coding: utf-8 -*-
"""
@author: aeb1
"""

from Steps import BaseStep as b
from Steps import Step3 as s

class Step2(b.BaseStep):
    def __init__(self, components):
        super().__init__(components)
    
    def entry(self):
        self.components.startTimer(4)
        self.components.lamps["LEFT_LOWER"].setState(True)
        self.components.lamps["RIGHT_LOWER"].setState(True)
        self.components.valves["LEFT_LOWER"].setState(True)
        self.components.valves["RIGHT_LOWER"].setState(True)
        self.components.valves["MIDDLE"].setState(True)
        super().entry()

    def exit(self):
        self.components.lamps["RIGHT_LOWER"].setState(False)
        self.components.lamps["LEFT_LOWER"].setState(False)  
        super().exit()

    def onSensor(self, sensorEvent):
        super().onSensor(sensorEvent)

    def onTimer(self):
        self.components.getCurrentStep().exit()
        self.components.setCurrentStep(s.Step3(self.components))
        #Hier sind alle Aktionen des Übergangs
        self.components.getCurrentStep().entry()
        super().onTimer()        
        
        