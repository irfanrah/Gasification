from numpy import arange, sin, pi
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import tkinter as Tk
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random
import time
import serial
#---------End of imports
Serial = serial.Serial('/dev/ttyUSB0', 9600) 


fig = plt.Figure(figsize = (5,4))
x = np.arange(0, 2*np.pi, 0.01)        

def ArduRead():
     ArduinoIn = str(Serial.readline()) 
     #ArduinoIn = "1212,31,24,12,3213"
     ArduinoCut = ArduinoIn[2:-5]
     ArduinoList = ArduinoCut.split(",")
     time.sleep(0.5) 
     return ArduinoList

def animate(i):
    line.set_ydata(np.sin(x+i/10.0))  # update the data
    return line,
    
def my_mainloop():
	Motor = ArduRead()
	Tk.Label(master=root, text=float(Motor[3]),font=("Helvetica", 25)).place(x = 50, y = 500)
	Tk.Label(master=root, text=float(Motor[2]),font=("Helvetica", 25)).place(x = 250, y = 500)
	Tk.Label(master=root, text=float(Motor[1]),font=("Helvetica", 25)).place(x = 480, y = 500)
	Tk.Label(master=root, text=float(Motor[0]),font=("Helvetica", 25)).place(x = 700, y = 500)
	
	Tk.Label(master=root, text="27 ",font=("Helvetica", 25)).place(x = 50, y = 600)
	Tk.Label(master=root, text="27 ",font=("Helvetica", 25)).place(x = 250, y = 600)
	Tk.Label(master=root, text="27 ",font=("Helvetica", 25)).place(x = 480, y = 600)
	Tk.Label(master=root, text="27 ",font=("Helvetica", 25)).place(x = 700, y = 600)
	print(Motor)
	root.after(100, my_mainloop)

	
	
root = Tk.Tk()
root.geometry("1200x1000")

root.after(100, my_mainloop)


label = Tk.Label(root,text="Gasification GUI Testing").grid(column=0, row=0)

canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().place(x=10, y=30)

ax = fig.add_subplot(111)
line, = ax.plot(x, np.sin(x))
ani = animation.FuncAnimation(fig, animate, np.arange(1, 200), interval=25, blit=False)

Tk.Label(master=root, text="Blower Hisap" ,font=("Helvetica", 18)).place(x = 10, y = 460)
Tk.Label(master=root, text="Blower Primer" ,font=("Helvetica", 18)).place(x = 210, y = 460)
Tk.Label(master=root, text="Vibrating Grate" ,font=("Helvetica", 18)).place(x = 410, y = 460)
Tk.Label(master=root, text="Screw Feeder" ,font=("Helvetica", 18)).place(x = 660, y = 460)

Tk.Label(master=root, text="Drying" ,font=("Helvetica", 18)).place(x = 10, y = 560)
Tk.Label(master=root, text="Pyrolisis" ,font=("Helvetica", 18)).place(x = 210, y = 560)
Tk.Label(master=root, text="Combustion" ,font=("Helvetica", 18)).place(x = 410, y = 560)
Tk.Label(master=root, text="Reduction" ,font=("Helvetica", 18)).place(x = 660, y = 560)

Tk.mainloop()
