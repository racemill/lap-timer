#!/usr/bin/python3

import time
import serial
import adafruit_thermal_printer

# Initialize thermal printer hardware serial connection on Raspberry Pi built-in UART:
uart = serial.Serial("/dev/serial0", baudrate=19200, timeout=3000)

# Import thermal printer module depending on version of printer firmware.  
ThermalPrinter = adafruit_thermal_printer.get_printer_class(2.19)

# Create the printer instance.
printer = ThermalPrinter(uart)

# Warm up and be ready to accept commands (calling it explicitly).
# printer.warm_up()

def header_config():
    printer.size = adafruit_thermal_printer.SIZE_LARGE
    printer.justify = adafruit_thermal_printer.JUSTIFY_CENTER
    printer.inverse = True

def body_config():
    printer.size = adafruit_thermal_printer.SIZE_MEDIUM
    printer.justify = adafruit_thermal_printer.JUSTIFY_LEFT
    printer.inverse = False
    printer.bold = True

def reset_config():
    printer.size = adafruit_thermal_printer.SIZE_SMALL
    printer.justify = adafruit_thermal_printer.JUSTIFY_LEFT
    printer.inverse = False
    printer.bold = False

def print_lap(laptime):
    printer.warm_up()
    lapdate = time.strftime("%a %m/%d/%y", time.localtime())
    header_config()
    printer.print("  Miller Trails ")
    body_config()
    printer.feed(1)
    printer.print("      O               /^^\     ")
    printer.print("     /\,            /^    ^^   ")
    printer.print("    -\ -       /^^^^ /^^    /^ ")
    printer.print("     /(*)  /^^^   /^^^   ^   ^^")
    printer.print("  (*) /^^^^   /^^^             ")
    printer.print("  ^^^^                         ")
    printer.print("  LAP: ",laptime)
    printer.print("    ",lapdate)
#    printer.feed(1)
    header_config()
    printer.print("   Great job!   ")
#   reset_config()
    printer.feed(4)

# print_lap("2:22")
