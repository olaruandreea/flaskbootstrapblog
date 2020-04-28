#!/bin/sh

# Script to kill python when the app is throwing "Address already in use"

LINE=$(ps -ef | grep "python run.py")
PROCESS=$(echo "$LINE" | awk '{print $2}')
kill -9 $PROCESS