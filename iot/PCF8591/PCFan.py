import smbus
import time
import math
import random

def readBus(address, pin):
    bus.write_byte(address,pin)
    return bus.read_byte(address)



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
    bus = smbus.SMBus(1)
    bus.write_byte_data(address,A0,250)
    setOfValue1.append(readBus(address, A1))
    setOfValue1.append(readBus(address, A2))
    setOfValue1.append(readBus(address, A3))
    setOfValue1.append(readBus(address, A4))
    
    
    bus = smbus.SMBus(4)
    bus.write_byte_data(address,A0,10)
    setOfValue2.append(readBus(address, A1))
    setOfValue2.append(readBus(address, A2))
    setOfValue2.append(readBus(address, A3))
    setOfValue2.append(readBus(address, A4))
    
    
    print("1 : " )
    print(setOfValue1)
    print("2 : ")
    print(setOfValue2)
    time.sleep(1)
    setOfValue1 = []
    setOfValue2 = []
    bus.close()
    



