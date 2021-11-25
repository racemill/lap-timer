#!/usr/bin/python3

import time
import sys
sys.path.append("/home/pi/.local/lib/python3.7/site-packages");
import board
import busio
from adafruit_ht16k33 import segments

# Create the I2C interface(GPIO pins used as output)
i2c = busio.I2C(board.SCL, board.SDA)

# Create the LED segment class(7 segment 4 character display)
display = segments.Seg7x4(i2c)

# Create the length of time to display lap time variable
display_duration = 30

def clearDisplay():
    display.fill(0)

def displayNumber(number):
    clearDisplay()
    #display.print(':')            # Turn on the : leds
    display.print(number)         # Display the lap time
    time.sleep(display_duration)  # Length of time to display the lap time
    clearDisplay()
