##### Lab 2 - Reaction Time
##### from CircuitPython Essentials Digital In Out example"""
import random #we need another library to generate a random timing
import time
import board
from digitalio import DigitalInOut, Direction, Pull

# LED setup on digital pin 6.
led = DigitalInOut(board.D6)
led.direction = Direction.OUTPUT

# Button setup on digital pin 5.
switch = DigitalInOut(board.D5)
switch.direction = Direction.INPUT

# variables to store information
ranDelay = 0.0 # random delay time in seconds
startTime = 0.0
rxnTime = 0.0 # start time and reaction time variables

while True:
    print("Push the button to start game")

    while switch.value == True:
        continue
        # wait for the user to push the button for start

    print("Get Ready!")
    time.sleep(1.0)
    print("Get Set!")
    time.sleep(1.0)
    ranDelay = random.random() * 5.0 # generate a random delay time 0 to 5 seconds
    time.sleep(ranDelay) # wait the random amount of time
    print("Go!")
    startTime = time.monotonic() # get the time
    led.value = True # turn on the LED

    while switch.value == True:
        continue
        # wait for the reaction button press

    led.value = False
    rxnTime = time.monotonic() - startTime
    print("Your time is ", rxnTime, " seconds.")
    time.sleep(2.0)