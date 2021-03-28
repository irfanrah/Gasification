

import tkinter as tk
from tkinter import *
import numpy as np
import random
import random
import matplotlib.pyplot as plt
from itertools import count
from matplotlib.animation import FuncAnimation
import random
import matplotlib.pyplot as plt
from itertools import count
from matplotlib.animation import FuncAnimation





def animate(i):
    x_vals.append(next(index))
    y_vals1.append(random.randint(0,100))
    y_vals2.append(random.randint(0,100))
    y_vals3.append(random.randint(0,100))
    y_vals4.append(random.randint(0,100))

    plt.plot(x_vals,y_vals1,label = 'line1')
    plt.plot(x_vals,y_vals2,label = 'line2')
    plt.plot(x_vals,y_vals3,label = 'line3' )
    plt.plot(x_vals,y_vals4,label = 'line4')

def my_mainloop():
    print("Hello World!")
    tk.Label(master=master, text="X", fg='green',bg = 'white',bd = '10' ,font=("Helvetica", 25)).place(x = 50, y = 495)
    tk.Label(master=master, text="Y", fg='blue',bg = 'white',bd = '10' , font=("Helvetica", 25)).place(x = 180, y = 495)
    tk.Label(master=master, text="Z", fg='red',bg = 'white',bd = '10' , font=("Helvetica", 25)).place(x = 310, y = 495)
    
    
    
    
    

    


master = tk.Tk()
master.title("Config")
master.geometry("1200x1000")

x_vals = []
y_vals1 = []
y_vals2 = []
y_vals3 = []
y_vals4 = []

plt.plot(x_vals,y_vals1,label = 'line1')
plt.plot(x_vals,y_vals2,label = 'line2')
plt.plot(x_vals,y_vals3,label = 'line3' )
plt.plot(x_vals,y_vals4,label = 'line4')
index = count()




master.after(1000, my_mainloop)


master.mainloop()
