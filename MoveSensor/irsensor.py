import sys
import time
import RPi.GPIO as gpio

gpio.setwarnings(False)
gpio.setmode(gpio.BOARD)
gpio.setup(7, gpio.IN)

def motion_detect():
	try:
		while True:
			if gpio.input(7)==1:
				time.sleep(0.5)
				print "modzraobaa!!!- "
	except KeyboardInterrupt:
		gpio.cleanup()
		print "\n terminated by user"
		sys.exit()
if __name__ == "__main__":
	motion_detect()
