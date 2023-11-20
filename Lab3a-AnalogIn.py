"""Lab 3 - Analog In
CircuitPython Essentials Analog In example"""
import time
import board
from analogio import AnalogIn

analog_pin = AnalogIn(board.A1)

while True:
    print(analog_pin.value) # the digital integer
    print(analog_pin.value * 3.3 / 65536) # the converted voltage
    time.sleep(0.1)