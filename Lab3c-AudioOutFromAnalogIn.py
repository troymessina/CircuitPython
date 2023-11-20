"""CircuitPython Essentials Analog In example"""
import time
import board
from analogio import AnalogIn
import audiocore
import audioio
import board
import array
import time
import math

# Generate one period of sine wav.
frequency = 440
length = 8000 // frequency
sine_wave = array.array("h", [0] * length)
for i in range(length):
    sine_wave[i] = int(math.sin(math.pi * 2 * i / length) * (2 ** 15))
sine_wave = audiocore.RawSample(sine_wave)
analog_pin = AnalogIn(board.A0)
audio = audioio.AudioOut(board.A1)

while True:
    #print(analog_pin.value) # the digital integer
    #print(analog_pin.value * 3.3 / 65536) # the converted voltage
    volts = analog_pin.value * 3.3 / 65536
    frequency = analog_pin.value // 50 + 200 #* 3300 // 65536 + 200
    length = 8000 // frequency
    print(analog_pin.value, frequency)
    sine_wave = array.array("h", [0] * length)
    for i in range(length):
        sine_wave[i] = int(math.sin(math.pi * 2 * i / length) * (2 ** 15))
    sine_wave = audiocore.RawSample(sine_wave)
    audio.play(sine_wave, loop=True)
    time.sleep(2.0)
    audio.stop()
