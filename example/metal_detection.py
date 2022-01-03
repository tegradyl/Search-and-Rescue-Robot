#!/usr/bin/env python3
"""
Program to integrate analog and US sensor for the metal detection and object, it displayed results over lego screen
"""
from time import sleep

from ev3dev2.sensor import INPUT_1
from ev3dev2.sensor.lego import UltrasonicSensor
from ev3dev2.sound import Sound

from robot import MetalDetector

SPACING = "|"
METAL = "Metal detected"
NOT_METAL = "Its not a metal"
NO_OBJECT = "Move on"

sound = Sound()
ss = MetalDetector(INPUT_1)
us = UltrasonicSensor()
us.mode = 'US-DIST-CM'

while True:
    analog_read = ss.analog_read
    distance = us.value()/10
    if distance == 255.0 and analog_read == 331.0:
        sleep(0.25)
        print('{}  {}  {}  {}'.format(float(analog_read), SPACING, float(distance), METAL))
        sleep(0.25)

    elif distance == 255.0 and analog_read == 516.0:
        sleep(0.5)
        print('{}  {}  {}  {}'.format(float(analog_read), SPACING, float(distance), NOT_METAL))
        sleep(0.25)

    elif distance != 255.0 and analog_read != 516.0 and analog_read != 331.0:
        sleep(0.25)
        print('{}  {}  {}  {}'.format(float(analog_read), SPACING, float(distance), NO_OBJECT))
        sleep(0.25)
