import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.IN)

for i in range(0,5):
    print GPIO.input(4)
