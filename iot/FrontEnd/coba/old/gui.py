

import tkinter as tk
from tkinter import *
import numpy as np
import random

master = tk.Tk()
master.title("Config")
master.geometry("1200x1000")

def my_mainloop():
    print("Hello World!")
    tk.Label(master=master, text="X", fg='green',bg = 'white',bd = '10' ,font=("Helvetica", 25)).place(x = 50, y = 495)
    tk.Label(master=master, text="Y", fg='blue',bg = 'white',bd = '10' , font=("Helvetica", 25)).place(x = 180, y = 495)
    tk.Label(master=master, text="Z", fg='red',bg = 'white',bd = '10' , font=("Helvetica", 25)).place(x = 310, y = 495)
    master.after(1000, my_mainloop)   #satuan milisecond 

master.after(1000, my_mainloop)

master.mainloop()
