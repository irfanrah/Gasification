from numpy import arange, sin, pi
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from pymodbus.client.sync import ModbusSerialClient as ModbusClient
from pymodbus.register_read_message import ReadInputRegistersResponse,ReadHoldingRegistersRequest
import tkinter as Tk
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random
import time
import serial

#ArduSerial = serial.Serial('/dev/ttyUSB0', 9600) 
#client = ModbusClient(method='rtu', bytesize = 8, baudrate = 9600,port="/dev/ttyUSB0", timeout=1,stopbits = 2, parity = 'N')

def ArduRead():
     #ArduinoIn = str(ArduSerial.readline()) 
     ArduinoIn = "1212,31,24,12,3213"
     ArduinoCut = ArduinoIn[2:-5]
     ArduinoList = ArduinoCut.split(",")
     time.sleep(0.5) 
     return ArduinoList

def TempRead():
	#result = client.read_input_registers(1000, 4, unit = 33)
	result = [30,0,30,0]
	return result





root = Tk.Tk()
root.title("Gasification GUI")
root.geometry("1200x1000")
root.configure(bg = 'white')


Tk.Label(master=root, text="Blower Hisap" ,font=("Helvetica", 22),bg = 'white').place(x = 20, y = 460)
Tk.Label(master=root, text="Blower Primer" ,font=("Helvetica", 22),bg = 'white').place(x = 230, y = 460)
Tk.Label(master=root, text="Vibrating Grate" ,font=("Helvetica", 22),bg = 'white').place(x = 430, y = 460)
Tk.Label(master=root, text="Screw Feeder" ,font=("Helvetica", 22), bg = 'white').place(x = 660, y = 460)

Tk.Label(master=root, text="Drying" ,font=("Helvetica", 22),bg = 'white').place(x = 70, y = 565)
Tk.Label(master=root, text="Pyrolisis" ,font=("Helvetica", 22),bg = 'white').place(x = 250, y = 565)
Tk.Label(master=root, text="Combustion" ,font=("Helvetica", 22),bg = 'white').place(x = 450, y = 565)
Tk.Label(master=root, text="Reduction" ,font=("Helvetica", 22),bg = 'white').place(x = 670, y = 565)


#if client.connect():
        #print("modbus connected*")


while(True):
    
	Motor = ArduRead()
	print("Test")
	Temperature = TempRead()
	
	Tk.Label(master=root, text=float(Motor[3]),font=("Helvetica", 20),bg = 'white', bd = '15').place(x = 50, y = 500)
	Tk.Label(master=root, text=float(Motor[2]),font=("Helvetica", 20),bg = 'white', bd = '15').place(x = 250, y = 500)
	Tk.Label(master=root, text=float(Motor[1]),font=("Helvetica", 20),bg = 'white', bd = '15').place(x = 480, y = 500)
	Tk.Label(master=root, text=float(Motor[0]),font=("Helvetica", 20),bg = 'white', bd = '15').place(x = 700, y = 500)
	
	Tk.Label(master=root, text=Temperature[0],font=("Helvetica", 20),bg = 'white', bd = '15').place(x = 80, y = 600)
	Tk.Label(master=root, text=Temperature[1],font=("Helvetica", 20),bg = 'white', bd = '15').place(x = 250, y = 600)
	Tk.Label(master=root, text=Temperature[2],font=("Helvetica", 20),bg = 'white', bd = '15').place(x = 480, y = 600)
	Tk.Label(master=root, text=Temperature[3],font=("Helvetica", 20),bg = 'white', bd = '15').place(x = 700, y = 600)
	time.sleep(0.3)
	
	root.update()
	
