#!/usr/bin/env python3

"""
License: You are free to use any part of code in this project as long as you mention original authors of this program:
Alpha Team composed of: Nirmalraj JEYANATHAN Joseph - SERFATY Milan - YE Hang - ZHANG Yujia

Supervised by Aurore (aurore.isep@gmail.com) and Hugo (myrobotswillconquertheworld@gmail.com)
IE.3510 (System Modeling) - ISEP 2022
"""

import time

from ev3dev2.sensor import INPUT_1

from robot import Robot

# Robot properties
ROBOT_LENGTH = 0
MOTOR_PORTS = {}
SENSOR_PORTS = {"ultrasonic_sensor": INPUT_1}

robot = Robot(ROBOT_LENGTH, MOTOR_PORTS, SENSOR_PORTS)

while True:
    print(robot.ultrasonic_sensor.value())
    time.sleep(1)
