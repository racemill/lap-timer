#!/usr/bin/python3

import RPi.GPIO as GPIO
import time
import threading
import datetime
import logging
import socket

BEAM_PORT = 20           # GPIO port for PhotoBeam
BEAM_TRIGGER_DELAY = 5	 # Min time between valid beam breaks to prevent false "quick" triggers
HOST = '192.168.50.5'    # IP of satellite raspi/segment display
PORT = 8084              # Port of satellite raspi/segment display
ADDR = (HOST,PORT)
BUFSIZE = 1024

last_lap_time = time.time()

def initialize():
     GPIO.setwarnings(False)         # Disable warning mesages for GPIO
     GPIO.setmode(GPIO.BCM)          # Set to use Boardcom pin numbering

     # Configure GPIO port as Input for PhotoBeam 
     # HW: PhotoBeam white wire to GPIO ground pin and black wire to GPIO port pin
     GPIO.setup(BEAM_PORT, GPIO.IN, pull_up_down=GPIO.PUD_UP) 

     # Detect PhotoBeam Breaks and then do callback to lap timer function
     GPIO.add_event_detect(BEAM_PORT, GPIO.RISING, callback=beam_callback, bouncetime=200)

def beam_callback(channel):
    #logging.info('BEAM Break Detected                           ')
    lapTime()

def lapTime():
     global last_lap_time

     now = time.time()
     time_since_last_lap = int(now - last_lap_time)
     tsll = time.strftime("%H:%M:%S", time.gmtime(time_since_last_lap))

     if time_since_last_lap < BEAM_TRIGGER_DELAY:
          #logging.info('   BEAM Break INVALID-TriggerDelay             ')
          return 429

     last_lap_time = now

     logging.info('LAP: %s   ' % tsll)

     # Send laptime to satellite raspi for display
     logging.info('Try to connect to satellite raspi ' )
     client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
     client.connect_ex(ADDR)
     logging.info('Try to send laptime to satellite raspi ' )
     client.send(tsll.encode())
     client.close()

     return 200

def cleanup():
     GPIO.cleanup()            # GPIO cleanup for a clean exit (reset ports used)

