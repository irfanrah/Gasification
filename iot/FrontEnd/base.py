#!/usr/bin/python3

import socket
import time
from pymodbus.client.sync import ModbusSerialClient as ModbusClient
from pymodbus.register_read_message import ReadInputRegistersResponse,ReadHoldingRegistersRequest
import random
import time
import serial
import xlsxwriter
from time import strftime 
import os
from datetime import datetime

counting = 0

def start_graph():
	
	return 0

def loop_graph(Motor,Temp,count,row):
	waktuUpdate = strftime("%H:%M:%S")
	worksheet.write(row, col, waktuUpdate)

	worksheet.write(row, col + 1, Motor[3]) # BH
	worksheet.write(row, col + 2, Motor[2]) 
	worksheet.write(row, col + 3, Motor[1])
	worksheet.write(row, col + 4, Motor[0]) 
	
	worksheet.write(row, col + 6, Temp[0]) # temp
	worksheet.write(row, col + 7, Temp[0])
	worksheet.write(row, col + 8, Temp[0])
	worksheet.write(row, col + 9, Temp[0])
	
	worksheet.write(row, col + 11, count)
	
def ArduRead():
     ArduSerial.flushInput()
     ArduinoIn = str(ArduSerial.readline()) 
     #ArduinoIn = "1212,31,24,12,3213"
     ArduinoCut = ArduinoIn[2:-5]
     ArduinoList = ArduinoCut.split(",")
     return ArduinoList

def TempRead():
	result = client.read_input_registers(1000, 4, unit = 33)
	return result.registers
	
def TempRead2():
	result = client.read_input_registers(1000, 1, unit = 34)
	return result.registers

def CalcBH(x):
	return round((0.4552306 + 0.04351914*x + 0.000005507515*x**2 + 3.982e-8*x**3),0)
	
def CalcBP(x): #udah 10sample
	return round((-0.1199131 + 0.0451825*x + 0.00002533928*x**2 - 1.243547e-8*x**3),0)
def CalcVG(x):
	return round((0.4552306 + 0.04351914*x + 0.000005507515*x**2 + 3.982e-8*x**3),0)
	
def CalcSF(x): # udah1 10 sample
	return round((-0.26705 + 0.04685134*x + 0.00003166803*x**2 - 3.975522e-8*x**3),0)

group = '224.1.1.1'
port = 5004

# 2-hop restriction in network
ttl = 2

sock = socket.socket(socket.AF_INET,
                     socket.SOCK_DGRAM,
                     socket.IPPROTO_UDP)
sock.setsockopt(socket.IPPROTO_IP,
                socket.IP_MULTICAST_TTL,
                ttl)
                
ArduSerial = serial.Serial('/dev/ttyUSB0', 9600) 
client = ModbusClient(method='rtu', bytesize = 8, baudrate = 9600,port="/dev/ttyUSB1", timeout=1,stopbits = 2, parity = 'N')


if client.connect():
        print("modbus connected*")
     

try :
	os.mkdir("Data")
except OSError:
	print("Folder Created")

path = "Data/"
waktu = strftime("%H:%M:%S")
tanggal = strftime("%d-%m-%Y")

# Create a workbook and add a worksheet.
workbook = xlsxwriter.Workbook(os.path.join(path , str(tanggal) + str(waktu)+'.xlsx'))
worksheet = workbook.add_worksheet()

# Some data we want to write to the worksheet.
worksheet.write(1, 2, 'Time')

worksheet.write(1, 3, 'Blower Hisap')
worksheet.write(1, 4, 'Blower Primer')
worksheet.write(1, 5, 'Vibrating Grate')
worksheet.write(1, 6, 'Screw Feeder')

worksheet.write(1, 8, 'Drying')
worksheet.write(1, 9, 'Pyrolisis')
worksheet.write(1, 10, 'Combustion')
worksheet.write(1, 11, 'Reduction')
worksheet.write(1, 13, 'Count')
row = 2
col = 2

while True:
	Motor = ArduRead()
	MotorConv = []
	Temperature = []
	TempCH33 = TempRead()
	TempCH34 = TempRead2()
	Temperature.append(TempCH33[0])
	Temperature.append(TempCH34[0])
	Temperature.append(TempCH33[2])
	Temperature.append(TempCH33[3])
	#print(float(Motor[0]))
	MotorConv.append(CalcSF(float(Motor[0])))
	MotorConv.append(CalcVG(float(Motor[1])))
	MotorConv.append(CalcBP(float(Motor[2])))
	MotorConv.append(CalcBH(float(Motor[3])))
	Datas = str(MotorConv) + "," + str(Temperature) + "," + str(counting)
	print(Datas)
	chat = bytes(Datas, "utf-8")
	sock.sendto(chat , (group, port))	
	counting = counting + 1
	try : 
		loop_graph(Motor,Temperature,counting,row)
		row = row + 1
		time.sleep(0.9)
	except KeyboardInterrupt:
		workbook.close()
		break

