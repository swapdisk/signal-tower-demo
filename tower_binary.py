#!/usr/bin/env python

import time
import RPi.GPIO as GPIO

"""
Define the GPIO pins to use. For the signal tower demo, pins are
assigned as follows:

Red    pin 7    GPIO 4
Amber  pin 11   GPIO 17
Green  pin 13   GPIO 27
Blue   pin 15   GPIO 22
"""
pins = [7,11,13,15]

"""
Cycle lights in a binary counting pattern. Ctrl-C will turn off
all lights and clean up.   
"""
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pins, GPIO.OUT)
try:
  i = 0
  while True:
    GPIO.output(pins, [i%2, (i>>1)%2, (i>>2)%2, (i>>3)%2])
    i += 1
    time.sleep(0.2)
except KeyboardInterrupt:
  GPIO.output(pins, 0)
  GPIO.cleanup()
