import random
import matplotlib.pyplot as plt
from itertools import count
from matplotlib.animation import FuncAnimation


#plt.style.use('fivethrityeight')

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

#plt.legend()
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



ani = FuncAnimation(plt.gcf(),animate,interval=100)

plt.tight_layout()
plt.show()