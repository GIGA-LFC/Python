import time  
import RPi.GPIO as GPIO  
  
GPIO.setmode(GPIO.BOARD)
GPIO.setup(3, GPIO.OUT)  
  
def RCtime (RCpin):  
        reading = 0  
        GPIO.setup(RCpin, GPIO.OUT)  
        GPIO.output(RCpin, GPIO.LOW)
	GPIO.setup(3, GPIO.OUT)  
        time.sleep(0.1)  
  
        GPIO.setup(RCpin, GPIO.IN)  
        while (GPIO.input(RCpin) == GPIO.LOW):  
                reading += 1  
        return reading  
	if(reading>2000):
		GPIO.output(3, GPIO.LOW)
		print "Relay is On!"
	elif(reading<20):
		GPIO.output(3, GPIO.HIGH)
  
while True:                                       
        print RCtime(11)  
