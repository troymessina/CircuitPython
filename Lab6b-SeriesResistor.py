"""CircuitPython Analog Out example"""
import array
import board
from analogio import AnalogOut
from analogio import AnalogIn
import time

Vout = AnalogOut(board.A0)
Vin = AnalogIn(board.A1)

V1 = array.array("d")
V2 = array.array("d")

for i in range(0, 65536, 8192):
    Vout.value = i
    time.sleep(0.25)
    V1.append(i*3.3/65535)
    V2.append(Vin.value/65535*3.3)
    time.sleep(0.05)
print("Vin")
print(V1)
time.sleep(0.05)
print("Vout")
print(V2)
