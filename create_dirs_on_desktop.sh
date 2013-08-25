#! /bin/bash

ITERATIONS=100
for i in `seq $ITERATIONS`; do mkdir /home/pi/Desktop/DIR$i ; done
sleep 3
for i in `seq $ITERATIONS`; do rm -rf /home/pi/Desktop/DIR$i ; done
