#!/usr/bin/python


import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BCM)

GPIO.setup(11, GPIO.IN)

x =1
while True:

	print GPIO.input(11) #// Reads the value from the Analog PIN 11
	
print "voice"
