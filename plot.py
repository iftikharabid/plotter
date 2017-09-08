import matplotlib.pyplot as plt
import numpy as np
import time
import sys

xaxis_range = 300

values1=[]
values1 = [0 for x in range(xaxis_range)]
values2=[]
values2 = [0 for x in range(xaxis_range)]


def LiveGraph(arg):
    global values, threshold
    xaxis = np.arange(len(values1)-xaxis_range, len(values1),1)
    line1[0].set_data(xaxis, np.array(values1[-xaxis_range:]))
    line2[0].set_data(xaxis, np.array(values2[-xaxis_range:]))
    ax.axis([xaxis.min(), xaxis.max(), -1.5,1.5])
    
    manager.canvas.draw()
    
    #line1[0].set_data(xaxis, np.array(values[-100:]))
def SignalGenerator(arg):
    global values1, values2

    randnum1 = np.random.rand(1)*2-1
    randum2 = (np.random.rand(1)*0.02)+0.5
    values1.append(randnum1)
    values2.append(randum2)

fig = plt.figure()
    #Set Timers
timer1=fig.canvas.new_timer(interval=100)
timer1.add_callback(LiveGraph, ())
timer2 = fig.canvas.new_timer(interval=100)
timer2.add_callback(SignalGenerator, ())
timer1.start()
timer2.start()


#plt.ion() # enable interactivity
xAchse=np.arange(0,100,1)
yAchse=np.array([0]*100)
ax = fig.add_subplot(111)
ax.grid(True)
ax.set_title("Realtime Randomized data")
ax.set_xlabel("Time")
ax.set_ylabel("Amplitude")
#ax.axis([0,200,-1.5,1.5])
line1=ax.plot(xAchse,yAchse,'-', linewidth=2)
line2=ax.plot(xAchse,yAchse,'-')
#setp(line2, linewidth=2, color='r')
manager = plt.get_current_fig_manager()
plt.show()
fig.show()
#plt.draw()     
#plt.pause(1)
#plt.show()
    