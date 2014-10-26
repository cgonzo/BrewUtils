#!/usr/bin/env python

import os
import time

def thermometerInit():
    # Set pullup on thermometer
    os.system("gpio -g mode 4 up")
    # wait for the thermometer to come up
    time.sleep(0.5)

def thermometerRead(serialNumber):
    # modified from https://www.cl.cam.ac.uk/projects/raspberrypi/tutorials/temperature/
    # Open the file that we viewed earlier so that python can see what is in it. Replace the serial number as before. 
    tfile = open("/sys/bus/w1/devices/"+serialNumber+"/w1_slave") 
    # Read all of the text in the file. 
    text = tfile.read() 
    # Close the file now that the text has been read. 
    tfile.close() 
    # Split the text with new lines (\n) and select the second line. 
    secondline = text.split("\n")[1] 
    # Split the line into words, referring to the spaces, and select the 10th word (counting from 0). 
    temperaturedata = secondline.split(" ")[9] 
    # The first two characters are "t=", so get rid of those and convert the temperature from a string to a number. 
    temperature = float(temperaturedata[2:]) 
    # Put the decimal point in the right place and display it. 
    temperature = temperature / 1000 
    return temperature

def test():
    thermometerInit()
    while 1:
        data = thermometerRead("28-00042d367bff")
        print data
        time.sleep(0.05)

test()
