from pymodbus.client.sync import ModbusSerialClient as ModbusClient
from pymodbus.register_read_message import ReadInputRegistersResponse,ReadHoldingRegistersRequest
import time



print("import ok")
client = ModbusClient(method='rtu', bytesize = 8, baudrate = 115200,port="/dev/ttyUSB0", timeout=3,strict = False, parity = 'N')
while(True):
    if client.connect():
        print("connected*")
        
    
    result = client.read_holding_registers(4000, 10, unit = 1)
    time.sleep(1)
    
    print(result.registers)
    print("********************************")
    
client.close()