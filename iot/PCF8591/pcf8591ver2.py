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
    
def BH(x):
    return round((0.5021822 + 0.167663*x + 0.0004566182*x**2 - 0.000001163124*x**3),0)

def BP(x):
    return round((-0.1774547 + 0.1785425*x + 0.0002470618*x**2 + 0.00000124362*x**3),0)


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
    #bus.write_byte_data(address,A0,250)
    setOfValue1.append(readBus(3,address,A2))
    setOfValue1.append(readBus(3,address,A3))
    setOfValue1.append(readBus(3,address,A4))
    
    
    #print("1 : ")
    #print(setOfValue1)
    time.sleep(1)
    BlowerHisap = setOfValue1[4]
    BlowerPrimer = setOfValue1[3]
    ScrewFeeder = setOfValue1[1]
    VibGrate = setOfValue1[2]
    
    print("BH " + str((BlowerHisap)))
    print("BP " + str((BlowerPrimer)))
    print("VG " + str(VibGrate))
    print("SF " + str(ScrewFeeder))
    
    setOfValue1 = []
