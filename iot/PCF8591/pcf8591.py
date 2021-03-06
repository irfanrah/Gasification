import smbus
import time
import math
import random

def readBus(SerialBus ,address, pin):
    global bus 
    bus = smbus.SMBus(SerialBus)
    bus.write_byte(address,pin)
    return bus.read_byte(address)

def writeBus(SerialBus ,address, pin,value):
    bus2 = smbus.SMBus(SerialBus)
    return bus2.write_byte(address,pin,value)
    
def Cacl1(input):
    return round((-0.2380388 + 0.02458734*input - 0.00001663521*input**2),2)

def Cacl2(input):
    return round((-0.0002679408 + 0.02006629*input + 0.000001552488*input**2),2)


address = 0x48
A0 = 0x40
A1 = 0x41
A2 = 0x42
A3 = 0x43
A4 = 0x44
#bus = smbus2.SMBus(4)

setOfValue1 = []
setOfValue2 = []
setOfValue3 = []
while True:
    value_out = random.randint(0,240)
    #writeBus(3,address,A0,value_out)
    setOfValue1.append(250)
    setOfValue1.append(readBus(3,address,A1))
    bus.write_byte_data(address,A0,250)
    setOfValue1.append(readBus(3,address,A2))
    setOfValue1.append(readBus(3,address,A3))
    setOfValue1.append(readBus(3,address,A4))
    
    setOfValue2.append(value_out)
    setOfValue2.append(readBus(4,address,A1))
    bus.write_byte_data(address,A0,value_out)
    setOfValue2.append(readBus(4,address,A2))
    setOfValue2.append(readBus(4,address,A3))
    setOfValue2.append(readBus(4,address,A4))   
    
    print("1 : ")
    print(setOfValue1)
    print("2 : ")
    print(setOfValue2)
    time.sleep(1)
    setOfValue1 = []
    setOfValue2 = []
    
