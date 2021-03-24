from pymodbus.client.sync import ModbusSerialClient as ModbusClient
from pymodbus.constants import Endian
from pymodbus.payload import BinaryPayloadDecoder
from pymodbus.payload import BinaryPayloadBuilder
import time

def validator(instance):
    if not instance.isError():
        '''.isError() implemented in pymodbus 1.4.0 and above.'''
        decoder = BinaryPayloadDecoder.fromRegisters(
            instance.registers,
            byteorder=Endian.Big, wordorder=Endian.Little
        )   
        return float('{0:.2f}'.format(decoder.decode_32bit_float()))

    else:
        # Error handling.
        print("There isn't the registers, Try again.")
        return None


print("import ok")

client = ModbusClient(method='rtu', bytesize = 8, baudrate = 115200,port="/dev/ttyUSB0", timeout=1)
while(True):
    if client.connect():
        print("connected*")
        
    # connection is OK
    # read floats
    #result = client.read_holding_registers(1, 1000, unit = 1)
    request = client.read_holding_registers(12482, 4, unit=1)
    
    #time.sleep(1)
    print(request)
    print("********************************")
    
client.close()