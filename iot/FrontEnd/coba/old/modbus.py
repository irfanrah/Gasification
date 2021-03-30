from pymodbus.client.sync import ModbusSerialClient as ModbusClient
from pymodbus.register_read_message import ReadInputRegistersResponse,ReadHoldingRegistersRequest
import time



print("import ok")
client = ModbusClient(method='rtu', bytesize = 8, baudrate = 9600,port="/dev/ttyUSB1", timeout=1,stopbits = 2, parity = 'N')
while(True):
    if client.connect():
        print("connected*")
        
    
    result = client.read_input_registers(1000, 4, unit = 33)
    time.sleep(1)
    
    print(result.registers)
    print("********************************")
    
client.close()
