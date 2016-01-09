#!/usr/bin/python


import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BCM)

GPIO.setup(3, GPIO.IN)


GPIO.input(3)
print "voice"
