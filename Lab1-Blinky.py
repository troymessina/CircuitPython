"""Lab 1 - Blinky
based on CircuitPython Essentials Digital Out example"""

import time
import board
from digitalio import DigitalInOut, Direction, Pull

# LED setup.
# You can connect an external LED instead. Suppose it is connected to digital pin 5
led = DigitalInOut(board.D6)
led.direction = Direction.OUTPUT

while True:
    led.value = True # turn the LED on
    # add a print statement so you can see when it is on and off in the Serial monitor
    time.sleep(1.0)  # wait seconds
    led.value = False # turn the LED off
    time.sleep(1.0) # wait seconds