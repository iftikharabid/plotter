import matplotlib.pyplot as plt
import numpy as np
import pylab
from pylab import *
import time
import sys

xaxis_range = 500
values1=[]
values1 = [0 for x in range(xaxis_range)]
values2=[]
values2 = [0 for x in range(xaxis_range)]


def LiveGraph(arg):
    global values, threshold
    xaxis = pylab.arange(len(values1)-xaxis_range, len(values1),1)
    line1[0].set_data(xaxis, pylab.array(values1[-xaxis_range:]))
    line2[0].set_data(xaxis, pylab.array(values2[-xaxis_range:]))
    ax.axis([xaxis.min(), xaxis.max(), -1.5,1.5])
    
    manager.canvas.draw()
    
    #line1[0].set_data(xaxis, pylab.array(values[-100:]))
def SignalGenerator(arg):
    global values1, values2
    temp1 = 0
    temp2 = 0
    temp3 = 0
    temp4 = 0
    temp5 = 0
    temp6 = 0

    randnum1 = random()*2-1
    randum2 = random()

    temp6 = temp5
    temp5 = temp4
    temp4 = temp3
    temp3 = temp2
    temp2 = temp1
    temp1 = (randum2 + temp1 + temp2 + temp3 + temp4 + temp5 + temp6)/7
    randum2 = random()

    values1.append(randnum1)
    values2.append(temp1)

fig = pylab.figure()
    #Set Timers
timer1=fig.canvas.new_timer(interval=100)
timer1.add_callback(LiveGraph, ())
timer2 = fig.canvas.new_timer(interval=100)
timer2.add_callback(SignalGenerator, ())
timer1.start()
timer2.start()


#plt.ion() # enable interactivity
xAchse=pylab.arange(0,100,1)
yAchse=pylab.array([0]*100)
ax = fig.add_subplot(111)
ax.grid(True)
ax.set_title("Realtime Randomized data")
ax.set_xlabel("Time")
ax.set_ylabel("Amplitude")
#ax.axis([0,200,-1.5,1.5])
line1=ax.plot(xAchse,yAchse,'-', linewidth=2)
line2=ax.plot(xAchse,yAchse,'-')
setp(line2, linewidth=2, color='r')
manager = pylab.get_current_fig_manager()
pylab.show()
fig.show()
#plt.draw()     
#plt.pause(1)
#plt.show()
    