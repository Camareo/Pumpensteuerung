# -*- coding: utf-8 -*-
"""
@author: aeb1
"""
     
class MainControl:
    def __init__(self) -> None:
        self.proxy = None
        self.components = None
    
    def setTanksystemProxy(self, tanksystemProxy):
        self.proxy = tanksystemProxy
        
    def setComponents(self, components):
        self.components = components

    def setPumpState(self, state) -> None:
        if state == 0:
            self.__setPumpState(False)
        else:
            self.__setPumpState(True)
        
    def __setPumpState(self, state) -> None:
        self.components.getPump().setState(state)

    def setValveState(self, position, state) -> None:
        if state.get() == 0:
            self.__setValveState(position, False)
        else:
            self.__setValveState(position, True)

    def __setValveState(self, position, state) -> None:
            self.components.getValve(position).setState(state)  

    def setLampState(self, position, state) -> None:
        if state.get() == 0:
           self.__setLampState(position, False)
        else:
            self.__setLampState(position, True)
 
    def __setLampState(self,position, state) -> None:
             self.components.getLamp(position).setState(state)  

    def reset(self) -> None:
        self.proxy.reset()

    def start(self) -> None:
        self.proxy.onStart()

    def exit(self, root) -> None:
        self.setPumpState(False)
        root.destroy()
        self.proxy.closeConnection()
