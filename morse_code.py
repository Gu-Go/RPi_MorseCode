import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

l1p = 18
l2p = 17
GPIO.setup(l1p,GPIO.OUT)
GPIO.setup(l2p,GPIO.OUT)

CODE = {'A': '.-',     'B': '-...',   'C': '-.-.', 
        'D': '-..',    'E': '.',      'F': '..-.',
        'G': '--.',    'H': '....',   'I': '..',
        'J': '.---',   'K': '-.-',    'L': '.-..',
        'M': '--',     'N': '-.',     'O': '---',
        'P': '.--.',   'Q': '--.-',   'R': '.-.',
     	'S': '...',    'T': '-',      'U': '..-',
        'V': '...-',   'W': '.--',    'X': '-..-',
        'Y': '-.--',   'Z': '--..',
        
        '0': '-----',  '1': '.----',  '2': '..---',
        '3': '...--',  '4': '....-',  '5': '.....',
        '6': '-....',  '7': '--...',  '8': '---..',
        '9': '----.' 
        }

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

	
TEXT = "ANIKET"

for character in list(TEXT):
	for element in CODE[character]:
		print(element)
		if element == '.':
			led1()
		elif element == '-':
			led2()
	time.sleep(2)
