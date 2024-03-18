# -*- coding: utf-8 -*-
"""
@author: aeb1
"""

#set filename for logger
import datetime

logFileName="output.txt" # Set the name of the log file
with open(logFileName, 'w') as file:
     file.write("LogFile: " + str(datetime.datetime.now()) + "\n")  # Open file and write to it
     
     
#set host for IP 
host = "localhost"
#host = "192.168.0.40"
#host ="192.168.0.42"