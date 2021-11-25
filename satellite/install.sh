#!/bin/bash
# Install script for satellite that receives lap times and displays them on segment display
# This system should have fixed IP of 192.168.50.5

LAPTIMER_PATH="/usr/local/lap-timer-satellite"
SYSTEMD_PATH="/etc/systemd/system"
USERBIN_PATH="/usr/bin"

LAPTIMER_SERVICE_FILE="lap-timer-satellite.service"

sudo mkdir -p $LAPTIMER_PATH
sudo cp *.py $LAPTIMER_PATH

sudo cp $LAPTIMER_SERVICE_FILE $SYSTEMD_PATH

sudo cp lt $USERBIN_PATH

sudo systemctl enable $LAPTIMER_SERVICE_FILE
sudo systemctl start $LAPTIMER_SERVICE_FILE
