from pymodbus.client.sync import ModbusSerialClient as ModbusClient
from pymodbus.register_read_message import ReadInputRegistersResponse,ReadHoldingRegistersRequest
import time



print("import ok")
client = ModbusClient(method='rtu', bytesize = 8, baudrate = 115200,port="/dev/ttyUSB0", timeout=3,strict = False, parity = 'N')
if client.connect():
    print("connected*")
    

result = client.read_coils(16389,10,unit=1)
print(result)

client.close()