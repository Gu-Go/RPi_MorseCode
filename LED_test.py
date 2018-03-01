import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

l1p = 18
l2p = 17
GPIO.setup(l1p,GPIO.OUT)
GPIO.setup(l2p,GPIO.OUT)


def led1():
	GPIO.output(l1p,GPIO.HIGH)
	time.sleep(1)
	GPIO.output(l1p,GPIO.LOW)	
	time.sleep(.5)
	print("LED1")

def led2():
	GPIO.output(l2p,GPIO.HIGH)
	time.sleep(1)
	GPIO.output(l2p,GPIO.LOW)	
	print("LED2")
	time.sleep(.5)

	

while (1):
	led1()
	led2() 
