import RPi.GPIO as GPIO
import time
import sys
import argparse
import os.path
import Morse

# Function that handles the arguments
def parseCommand():
	parse = argparse.ArgumentParser()
	parse.add_argument("text")
	parse.add_argument("-D", "--debug", action="store_true", help="Output Debug Messages")
	parse.add_argument("-d", "--dit", type=float, default=0.3, help="Defines the duration of a short light")
	parse.add_argument("-g", "--gpio", type=int, default=4, help="Choose the GPIO to control")
	parse.add_argument("-c", "--code", default="morseCode.cod", help="File that has the code")
	return parse.parse_args()

def main():
	# Parse the Commandline
	args = parseCommand()
	DEBUG = args.debug	
	LED = args.gpio
	DIT = args.dit
	DAH = 3*DIT

	# Setup the converter
	try:
		morseConverter = Morser.Converter(args.code)
	except IOError:
		return 1

	# Setup the GPIO-Pins		
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(LED,GPIO.OUT)
	GPIO.output(LED, GPIO.LOW)

	if DEBUG:
		print vars(args)
	
	# let the LED blink
	for word in args.text:
		# TODO put this in its function 
		for letter in word:
			sequence = morseConverter.toMorse(letter)
			if DEBUG:
				print sequence
			for light in sequence:
				GPIO.output(LED, GPIO.HIGH)
				if light == ".":
					time.sleep(DIT)
				else:
					time.sleep(DAH)
				GPIO.output(LED, GPIO.LOW)
				time.sleep(DIT)
			time.sleep(2*DIT)
		time.sleep(4*DIT)
		if DEBUG:
			print " "
	GPIO.cleanup()

# Have a main function
if __name__ == "__main__":
	sys.exit(main())
