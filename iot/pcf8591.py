import smbus2
import time
import math

def readBus(address, pin):
    bus.write_byte(address,pin)
    return bus.read_byte(address)

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
bus = smbus2.SMBus(1)

setOfValue = []
while True:
    setOfValue.append(Cacl1(readBus(address,A0)))
    setOfValue.append(Cacl1(readBus(address,A1)))
    setOfValue.append(Cacl2(readBus(address,A2)))
    setOfValue.append(Cacl2(readBus(address,A3)))
    setOfValue.append(Cacl2(readBus(address,A4)))
    print(setOfValue)
    time.sleep(0.5)
    setOfValue = []