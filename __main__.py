#!/usr/bin/env python3
"""This script makes the decision for the cars movements"""
from __future__ import division
import time
import sys

from HRSR04 import DistanceSensor
from vehicle import Car

# create two distance sensor's
LEFTSENSOR = DistanceSensor(23, 24)
RIGHTSENSOR = DistanceSensor(18, 27)

# add new car, left servo on channel 0 and right servo on channel 1
SMARTCAR = Car(0, 1)

def main():
	DELAY = 0.75
	#"""
	print("--------------------")
	time.sleep(0.1)

	LEFT_DISTANCE = LEFTSENSOR.distance()
	RIGHT_DISTANCE = RIGHTSENSOR.distance()

	print("left:  ", LEFT_DISTANCE)
	print("right: ", RIGHT_DISTANCE)
	#"""

	#"""
	if LEFT_DISTANCE < 10 and RIGHT_DISTANCE < 10:
		if LEFT_DISTANCE < 4 or RIGHT_DISTANCE < 4:
			SMARTCAR.move_backward()
			time.sleep(DELAY)
		else:
			if LEFT_DISTANCE < RIGHT_DISTANCE:
				SMARTCAR.move_right()
				time.sleep(DELAY)
			else:
				SMARTCAR.move_left()
				time.sleep(DELAY)
	elif LEFT_DISTANCE < 10:
		SMARTCAR.move_left()

	elif RIGHT_DISTANCE < 10:
		SMARTCAR.move_right()
	else:
		SMARTCAR.move_forward()
	#"""

while True:
	try:
		main()
	except KeyboardInterrupt:
		print("Interrupted")
		SMARTCAR.move_stop()
		sys.exit(0)
