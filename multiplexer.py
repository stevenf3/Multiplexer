import numpy as np
import u6
from GUIBaseClasses import *

d = u6.U6()
input_pins = ['EIO0', 'EIO1','EIO2','EIO3']

reading_pin = 5
mux_0 = [0,0,0,0]
mux_1 = [1,0,0,0]
mux_2 = [0,1,0,0]
mux_3 = [1,1,0,0]
mux_4 = [0,0,1,0]
mux_5 = [1,0,1,0]
mux_6 = [0,1,1,0]
mux_7 = [1,1,1,0]
mux_8 = [0,0,0,1]
mux_9 = [1,0,0,1]
mux_10 = [0,1,0,1]
mux_11 = [1,1,0,1]
mux_12 = [0,0,1,1]
mux_13 = [1,0,1,1]
mux_14 = [0,1,1,1]
mux_15 = [1,1,1,1]
output_pins = [mux_0,mux_1,mux_2,mux_3,mux_4,mux_5,mux_6,mux_7,mux_8,mux_9,mux_10,mux_11,mux_12,mux_13,mux_14,mux_15]

def muxer(reading_pin, DIOPinList):
    print(reading_pin, output_pins[reading_pin])
    for i in range(0,20):
        d.getFeedback(u6.BitStateWrite(i, 0))
    for pin in DIOPinList:
        if pin.startswith('E'):
            IONumber = int(pin[3:]) + 8
        elif pin.startswith('C'):
            IONumber = int(pin[3:]) + 16
        elif pin.startswith('M'):
            IONumber = int(pin[3:]) + 16
        else:
            IONumber = int(pin[3:])
        d.getFeedback(u6.BitDirWrite(int(IONumber), 1))
        if output_pins[reading_pin][DIOPinList.index(pin)] == 1:
            d.getFeedback(u6.BitStateWrite(int(IONumber), 1))
            print("%s, S%s, IONumber: %s, set to HI" % (pin, str(DIOPinList.index(pin)), str(IONumber)))
        else:
            print("%s, S%s, IONumber: %s, set to LO" % (pin, str(DIOPinList.index(pin)), str(IONumber)))

    reading = d.getAIN(0)
    return(reading)

print(muxer(15, input_pins))
