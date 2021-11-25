#!/bin/bash

LAPTIMER_PATH="/usr/local/lap-timer"
SYSTEMD_PATH="/etc/systemd/system"
USERBIN_PATH="/usr/bin"

LAPTIMER_SERVICE_FILE="lap-timer.service"

sudo mkdir -p $LAPTIMER_PATH
sudo cp *.py $LAPTIMER_PATH
sudo cp index.html $LAPTIMER_PATH

sudo cp $LAPTIMER_SERVICE_FILE $SYSTEMD_PATH

sudo cp ld $USERBIN_PATH
sudo cp le $USERBIN_PATH
sudo cp lt $USERBIN_PATH

sudo systemctl enable $LAPTIMER_SERVICE_FILE
sudo systemctl start $LAPTIMER_SERVICE_FILE

