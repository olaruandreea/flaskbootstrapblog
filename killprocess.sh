#!/bin/sh

LINE=$(ps -ef | grep "python run.py")
PROCESS=$(echo "$LINE" | awk '{print $2}')
kill -9 $PROCESS