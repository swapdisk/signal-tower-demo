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
Define an attention-getting light sequence pattern.
"""
num = 32
seq = [
  [1,0,0,0],
  [0,1,0,0],
  [0,0,1,0],
  [0,0,0,1],
  [0,0,1,0],
  [0,1,0,0],
  [1,0,0,0],
  [0,1,0,0],
  [0,0,1,0],
  [0,0,0,1],
  [0,0,1,0],
  [0,1,0,0],
  [0,0,0,0],
  [1,1,1,1],
  [0,0,0,0],
  [1,1,1,1],
  [0,0,0,0],
  [1,1,1,1],
  [0,0,0,0],
  [1,1,1,1],
  [0,0,0,0],
  [0,1,0,1],
  [1,0,1,0],
  [0,1,0,1],
  [1,0,1,0],
  [0,1,0,1],
  [1,0,1,0],
  [0,1,0,1],
  [0,0,0,0],
  [1,1,1,1],
  [1,1,1,0],
  [1,1,0,0]
]

"""
Cycle lights using the attention-getting pattern. Ctrl-C will turn off
all lights and clean up.   
"""
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pins, GPIO.OUT)
try:
  i = 0
  while True:
    GPIO.output(pins, seq[i%num])
    i += 1
    time.sleep(0.1)
except KeyboardInterrupt:
  GPIO.output(pins, 0)
  GPIO.cleanup()
