import RPi.GPIO as GPIO
from time import sleep     # this lets us have a time delay (see line 15)
GPIO.setmode(GPIO.BCM)     # set up BCM GPIO numbering
GPIO.setup(25, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # set GPIO25 as input (button)
GPIO.setup(24, GPIO.OUT)   # set GPIO24 as an output (LED)

prev_input = 0

try:
    while True:            # this will carry on until you hit CTRL+C
        curr_input = GPIO.input(25)
        if ((not prev_input) and curr_input):  # if port 25 == 1 and it was previously 0
            print("Port 25 is 1/HIGH/True - BUTTON PRESSED")
            GPIO.output(24, (not GPIO.input(24)))         # Toggle pin 24 - set port/pin value to 1/HIGH/True
        prev_input = curr_input
        sleep(0.1)         # wait 0.1 seconds

finally:                   # this block will run no matter how the try block exits
    GPIO.cleanup()         # clean up after yourself
