#!/usr/bin/env python3
from time import sleep
import os
import signal
import sys
import RPi.GPIO as GPIO
pin = 14 # The pin ID, edit here to change it
maxTMP = 54 # The maximum temperature in Celsius after which we trigger the fandef setup():
minTMP = 40
sleepTime = 5
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)
def getCPUtemperature():
    res = os.popen("vcgencmd measure_temp").readline()
    temp =(res.replace("temp=","").replace("'C\n",""))
#    print("temp is {0}".format(temp)) #Uncomment here for testing
    return temp
def fanON():
    setPin(True)
    return()
def fanOFF():
    setPin(False)
    return()
def getTEMP():
    CPU_temp = float(getCPUtemperature())
    if CPU_temp>maxTMP:
        fanON()
    elif CPU_temp<minTMP:
        fanOFF()
    return()
def setPin(mode): # A little redundant function but useful if you want to add logging
    GPIO.output(pin, mode)
    return()
try:
    while True:
        getTEMP()
        sleep(5)
except KeyboardInterrupt: # trap a CTRL+C keyboard interrupt 
    GPIO.cleanup() # resets all GPIO ports used by this program
