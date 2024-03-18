# -*- coding: utf-8 -*-
"""
@author: aeb1
"""
from Steps import BaseStep as b
from Steps import Step2 as s

class Step1(b.BaseStep):
    def __init__(self, components):
        super().__init__(components)
    
    def entry(self):
        self.components.lamps["LEFT_LOWER"].setState(False)
        self.components.lamps["RIGHT_LOWER"].setState(False)
        self.components.lamps["LEFT_UPPER"].setState(True)
        self.components.lamps["RIGHT_UPPER"].setState(True)
        self.components.valves["LEFT_UPPER"].setState(True)
        self.components.valves["RIGHT_UPPER"].setState(True)
        self.components.valves["MIDDLE"].setState(True)
        self.components.valves["LEFT_LOWER"].setState(False)
        self.components.valves["RIGHT_LOWER"].setState(False)
        self.components.pump.setState(True)
        super().entry()

    def exit(self):
        self.components.lamps["LEFT_UPPER"].setState(False)
        self.components.lamps["RIGHT_UPPER"].setState(False)
        self.components.pump.setState(False)
        super().exit()
        
    def onSensor(self, sensorEvent):
        if str(sensorEvent).strip() == "sensor_right_middle wet":
            self.components.getCurrentStep().exit()
            self.components.setCurrentStep(s.Step2(self.components))
            #hier kommen alle Actions des Zustandsübergangs hin, falls vorhanden 
            self.components.getCurrentStep().entry()
        if str(sensorEvent).strip() == "sensor_bottom_lower dry":
            self.components.pump.setState(False)
        super().onSensor(sensorEvent)

    def onTimer(self):
        super().onTimer()
        