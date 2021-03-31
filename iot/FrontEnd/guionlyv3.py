from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import tkinter as Tk
import numpy as np
import matplotlib.pyplot as plt
import time
import socket
import struct
import re

##mungkin delaynya diubah lagi karna sebelum write excel 0.5 sekarang 0.9	


MCAST_GRP = '224.1.1.1'
MCAST_PORT = 5004

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

sock.bind(('', MCAST_PORT))
mreq = struct.pack("4sl", socket.inet_aton(MCAST_GRP), socket.INADDR_ANY)

sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)




	
def decoding():
    msg = sock.recv(64)
    msgd = msg.decode("utf-8")
    digilist =  re.findall('\d+', msgd )
    Motor = digilist[0:4]
    Temperature = digilist[4:8]
    count = digilist[8]
    return Motor,Temperature,count


	

def my_mainloop():
	Motor, Temperature,count = decoding()
	Tk.Label(master=root, text=Motor[3],font=("Helvetica", 20),bg = 'white', bd = '15').place(x = 50, y = 500)
	Tk.Label(master=root, text=Motor[2],font=("Helvetica", 20),bg = 'white', bd = '15').place(x = 250, y = 500)
	Tk.Label(master=root, text=count,font=("Helvetica", 20),bg = 'white', bd = '15').place(x = 480, y = 500)
	Tk.Label(master=root, text=Motor[0],font=("Helvetica", 20),bg = 'white', bd = '15').place(x = 700, y = 500)

	Tk.Label(master=root, text=Temperature[0],font=("Helvetica", 20),bg = 'white', bd = '15').place(x = 80, y = 600)
	Tk.Label(master=root, text=Temperature[1],font=("Helvetica", 20),bg = 'white', bd = '15').place(x = 250, y = 600)
	Tk.Label(master=root, text=Temperature[2],font=("Helvetica", 20),bg = 'white', bd = '15').place(x = 480, y = 600)
	Tk.Label(master=root, text=Temperature[3],font=("Helvetica", 20),bg = 'white', bd = '15').place(x = 700, y = 600)
	time.sleep(0.1)
	
	root.after(100, my_mainloop)



root = Tk.Tk()
root.title("Gasification GUI")
root.geometry("1200x1000")
root.configure(bg = 'white')
root.after(100, my_mainloop)

Tk.Label(master=root, text="Blower Hisap" ,font=("Helvetica", 22),bg = 'white').place(x = 20, y = 460)
Tk.Label(master=root, text="Blower Primer" ,font=("Helvetica", 22),bg = 'white').place(x = 230, y = 460)
Tk.Label(master=root, text="Vibrating Grate" ,font=("Helvetica", 22),bg = 'white').place(x = 430, y = 460)
Tk.Label(master=root, text="Screw Feeder" ,font=("Helvetica", 22), bg = 'white').place(x = 660, y = 460)

Tk.Label(master=root, text="Drying" ,font=("Helvetica", 22),bg = 'white').place(x = 70, y = 565)
Tk.Label(master=root, text="Pyrolisis" ,font=("Helvetica", 22),bg = 'white').place(x = 250, y = 565)
Tk.Label(master=root, text="Combustion" ,font=("Helvetica", 22),bg = 'white').place(x = 450, y = 565)
Tk.Label(master=root, text="Reduction" ,font=("Helvetica", 22),bg = 'white').place(x = 670, y = 565)


Tk.mainloop()


