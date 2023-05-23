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
All lights off
"""
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pins, GPIO.OUT)
GPIO.output(pins, [0, 0, 0, 0])
