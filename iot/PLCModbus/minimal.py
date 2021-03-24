import minimalmodbus
import time

PORT='/dev/ttyUSB0'


#Set up instrument
instrument = minimalmodbus.Instrument(PORT,1,mode=minimalmodbus.MODE_RTU)

#Make the settings explicit
instrument.serial.baudrate = 115200        # Baud
instrument.serial.bytesize = 8
instrument.serial.parity   = minimalmodbus.serial.PARITY_NONE
instrument.serial.stopbits = 1
instrument.serial.timeout  = 1          # seconds

# Good practice
instrument.close_port_after_each_call = True

instrument.clear_buffers_before_each_transaction = True
# Read temperatureas a float
# if you need to read a 16 bit register use instrument.read_register()
#temperature = instrument.read_float(TEMP_REGISTER)

# Read the humidity
#humidity = instrument.read_float(HUM_REGISTER)

#Pront the values
print("lopp")
while True:
    time.sleep(.05)

        # function 3
    energy_all = instrument.read_string(0x0,1, 4)
    print("clear")

    time.sleep(1)