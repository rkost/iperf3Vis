#!/bin/bash

sleep 60

FILE=/home/rkost/speedtests/iperf-$(date +%Y-%m-%d-%H-%M-%S).json && iperf3 -c speedtest.wtnet.de -4 -t 20 -i 1 -b 60M -p 5208 --json --logfile $FILE

