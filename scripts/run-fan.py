#!/usr/bin/env python3

from time import sleep
import os
import RPi.GPIO as GPIO

pin = 14 # GPIO pin
maxTMP = 59 # The temperature in Celsius after which we trigger the fan
minTMP = 40 # The temperature in Celsius after which we stop the fan
sleepTime = 5
debug = False

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)
def getCPUtemperature():
    res = os.popen("vcgencmd measure_temp").readline()
    temp =(res.replace("temp=","").replace("'C\n",""))
    if (debug):
        print("temp is {0}".format(temp)) #Uncomment here for testing

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

def setPin(mode):
    GPIO.output(pin, mode)
    return()

try:
    while True:
        getTEMP()
        sleep(5)
except KeyboardInterrupt: # trap a CTRL+C keyboard interrupt 
    GPIO.cleanup() # resets all GPIO ports used by this program
