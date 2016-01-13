#!/usr/bin/python


import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BCM)

GPIO.setup(7, GPIO.IN)


for i in range(100)
	a = GPIO.input(7) #// Reads the value from the Analog PIN A0
	print a
print "voice"
