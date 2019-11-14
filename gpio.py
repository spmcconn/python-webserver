import RPi.GPIO as GPIO
import requests
from datetime import datetime
from time import sleep     # this lets us have a time delay (see line 15)
GPIO.setmode(GPIO.BCM)     # set up BCM GPIO numbering
# set GPIO25 as input (button)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(25, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
# GPIO.setup(24, GPIO.OUT)   # set GPIO24 as an output (LED)

prev_input23 = 0
prev_input24 = 0
prev_input25 = 0

try:
    while True:            # this will carry on until you hit CTRL+C
        if(GPIO.input(23) == True):
            if (not prev_input23):  # if port 23 == 1 and it was previously 0
                print("Port 23 is 1/HIGH/True - BUTTON PRESSED")
                payload = { "date": datetime.now(), "list": "kitties" }
                r = requests.post("http://192.168.0.104/post", data = payload)
                print(r.text)
                # GPIO.output(24, (not GPIO.input(24)))         # Toggle pin 24 - set port/pin value to 1/HIGH/True
            prev_input23 = True
        else:
            prev_input23 = False

        if(GPIO.input(24) == True):
            if (not prev_input24):  # if port 24 == 1 and it was previously 0
                print("Port 24 is 1/HIGH/True - BUTTON PRESSED")
                payload = { "date": datetime.now(), "list": "andi" }
                r = requests.post("http://192.168.0.104/post", data = payload)
                print(r.text)
                # GPIO.output(24, (not GPIO.input(24)))         # Toggle pin 24 - set port/pin value to 1/HIGH/True
            prev_input24 = True
        else:
            prev_input24 = False

        if(GPIO.input(25) == True):
            if (not prev_input25):  # if port 25 == 1 and it was previously 0
                print("Port 25 is 1/HIGH/True - BUTTON PRESSED")
                payload = { "date": datetime.now(), "list": "addison" }
                r = requests.post("http://192.168.0.104/post", data = payload)
                print(r.text)
                # GPIO.output(24, (not GPIO.input(24)))         # Toggle pin 24 - set port/pin value to 1/HIGH/True
            prev_input25 = True
        else:
            prev_input25 = False

        sleep(0.1)

        # curr_input = GPIO.input(25)
        # if ((not prev_input) and curr_input):  # if port 25 == 1 and it was previously 0
        #     print("Port 25 is 1/HIGH/True - BUTTON PRESSED")
        #     payload = { "date": datetime.now() }
        #     r = requests.post("http://192.168.0.104/post", data = payload)
        #     print(r.text)
        #     #GPIO.output(24, (not GPIO.input(24)))         # Toggle pin 24 - set port/pin value to 1/HIGH/True
        # prev_input = curr_input
        # sleep(0.1)         # wait 0.1 seconds
    
except requests.exceptions.RequestException as e:
    print(e)

finally:                   # this block will run no matter how the try block exits
    GPIO.cleanup()         # clean up after yourself
