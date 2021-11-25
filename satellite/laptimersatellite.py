#!/usr/bin/python3
# Configure Socket to receive lap times from laptimer, display on 7 Segment Display and print if the toggle switch is on.

import time
import threading
import logging
import segment
import socket
import printer
import RPi.GPIO as GPIO

HOST = '0.0.0.0'
PORT = 8084
ADDR = (HOST,PORT)
BUFSIZE = 1024
SWITCH = 24

# Setup logging 
logging.basicConfig(filename='/var/log/lap-timer-satellite.log', format=' %(message)s %(asctime)s', datefmt='%I:%M:%S %p %m/%d/%Y', level=logging.DEBUG)

# Setup listening socket for connections from laptimer
serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv.bind(ADDR)
serv.listen(5)
logging.info('listening ..................................')

# Setup GPIO port for toggle switch that controls if laptimes are printed. (3.3v to GPIO pin using built in pull down resistor)
GPIO.setmode(GPIO.BCM)
GPIO.setup(SWITCH, GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

while True:
      conn, addr = serv.accept()
      #logging.info('Client connected ...%s ', addr)
        
      data = conn.recv(BUFSIZE)
      laptime = (data.decode("utf-8"))
            
      conn.close()
      #logging.info('Lap Time:.. %s........................' % laptime)

      x = threading.Thread(target=segment.displayNumber, args=(laptime,))
      x.start()
      if (GPIO.input(SWITCH)):     # If HW toggle switch is On
          printer.print_lap(laptime)
