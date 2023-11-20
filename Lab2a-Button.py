"""Lab 2 - Buttons
from CircuitPython Essentials Digital In Out example"""
import time
import board
from digitalio import DigitalInOut, Direction, Pull

# LED setup on digital pin 6.
led = DigitalInOut(board.D6)
led.direction = Direction.OUTPUT

# Button setup on digital pin 5.
switch = DigitalInOut(board.D5)
switch.direction = Direction.INPUT

while True:
    # We could also do "led.value = not switch.value"!
    if not switch.value:
        led.value = True
        print("LED on")
    else:
        led.value = False
        print("LED off")

    time.sleep(0.01)  # debounce delay