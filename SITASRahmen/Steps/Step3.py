# -*- coding: utf-8 -*-
"""
@author: aeb1
"""

from Steps import BaseStep as b
from Steps import Step1 as s

class Step3(b.BaseStep):
    def __init__(self, components):
        super().__init__(components)
    
    def entry(self):
        self.components.lamps["LEFT_LOWER"].setState(False)  
        self.components.lamps["RIGHT_LOWER"].setState(False)
        super().entry()

    def exit(self):
        super().exit()

    def onSensor(self, sensorEvent):
        if str(sensorEvent).strip() == "sensor_left_lower dry":
            self.components.nextRepetition()
            if self.components.repetition <= 2:
                self.components.getCurrentStep().exit()
                self.components.setCurrentStep(s.Step1(self.components))
                #Hier sind alle Aktionen des Übergangs
                self.components.pump.setState(True)
                self.components.getCurrentStep().entry()
        super().onSensor(sensorEvent)

    def onTimer(self):
        super().onTimer()        
        
        