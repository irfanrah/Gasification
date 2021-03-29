import numpy as np
import matplotlib.pyplot as plt
import random
from itertools import count

x_vals = []
y_vals1 = []
y_vals2 = []
y_vals3 = []
y_vals4 = []

fig1, ax1 = plt.subplots()

fig2, ax2 = plt.subplots()


ax1.plot(x_vals,y_vals1,label = 'line1')
ax1.plot(x_vals,y_vals2,label = 'line2')
ax1.plot(x_vals,y_vals3,label = 'line3' )
ax1.plot(x_vals,y_vals4,label = 'line4')

plt.ion()
plt.show()


ax2.plot(x_vals,y_vals1,label = 'line1')
ax2.plot(x_vals,y_vals2,label = 'line2')


plt.show()


index = count()
while True:
    x_vals.append(next(index))
    y_vals1.append(random.randint(0,100))
    y_vals2.append(random.randint(0,100))
    y_vals3.append(random.randint(0,100))
    y_vals4.append(random.randint(0,100))
    
    ax1.plot(x_vals,y_vals1,label = 'line1')
    ax1.plot(x_vals,y_vals2,label = 'line2')
    ax1.plot(x_vals,y_vals3,label = 'line3' )
    ax1.plot(x_vals,y_vals4,label = 'line4')
    
    plt.draw()
    plt.pause(0.1)
    
    
    ax2.plot(x_vals,y_vals1,label = 'line1')
    ax2.plot(x_vals,y_vals2,label = 'line2')
    
    plt.draw()
    plt.pause(0.1)
    

