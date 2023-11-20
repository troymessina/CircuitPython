"""Lab 3 - Audio Out"""
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

audio = audioio.AudioOut(board.A1)
sine_wave = audiocore.RawSample(sine_wave)
audio.play(sine_wave, loop=True)
time.sleep(5)
audio.stop()