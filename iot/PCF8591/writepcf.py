import smbus
import time
import random

address = 0x48
cmd = 0x40
value = 0

bus = smbus.SMBus(4)
while True:
    bus.write_byte_data(address,cmd,value)
    value = random.randint(0,250)
    if value == 256:
        value =0
    print("AOUT:%3d" %value)
    time.sleep(1)
