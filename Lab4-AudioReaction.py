"""Lab 4 - Audio Reaction Time"""
import time #keep track of time and make delays
import random
import array #store lists of values
import math #do math like sine, cosine
import audiocore
import audioio #create sounds
import board #identify the microcontroller
from digitalio import DigitalInOut, Direction, Pull #do digital I/O

# Button setup on digital pin 6.
switch = DigitalInOut(board.D6)
switch.direction = Direction.INPUT
# Create a sine wave for audio output
tone_volume = 1.0  # Increase this to increase the volume of the tone.
frequency = 440  # Set this to the Hz of the tone you want to generate.
length = 8000 // frequency
sine_wave = array.array("h", [0] * length)
for i in range(length):
    sine_wave[i] = int(math.sin(math.pi * 2 * i / length) * (2 ** 15))

audio = audioio.AudioOut(board.A1)
sine_wave = audiocore.RawSample(sine_wave)

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
    audio.play(sine_wave, loop=True) #play the sound

    while switch.value == True:
        continue
        # wait for the reaction button press

    audio.stop() # turn off the audio
    rxnTime = time.monotonic() - startTime # calculate the reaction time
    print("Your time is ", rxnTime, " seconds.")
    time.sleep(2.0)