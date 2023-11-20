import time #keep track of time and make delays
import board #identify the microcontroller
import analogio #do analog I/O
import array #make lists of numbers

Vin = analogio.AnalogOut(board.A0) #apply analog output on A0
V2 = analogio.AnalogIn(board.A1) #read analog input on A1
V1_arr = array.array("d")#create an array of V1
I_arr = array.array("d") #create an array of current
Vin_list = [0.5, 1.0, 1.5, 2.0, 2.5, 3.0] #list of Vin

for i in Vin_list: #loop to scan input voltage
    #Students edit the following four lines
    Vin.value = int(i*65535/3.3)#conversion to integer using i in place of Vin
    time.sleep(0.2)
    V2Volts = V2.value*3.3/65535#conversion of V2 from integer to volts using V2.value
    V1_arr.append(i - V2Volts) # calculation of V1 using i as Vin and V2Volts
    I_arr.append(V2Volts/4.7) # conversion of V2 to current using R2 and V2Volts
    time.sleep(0.2)

#print the results
print("V1")
print(V1_arr)
print("I")
print(I_arr)
