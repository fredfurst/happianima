##
## Matplotlib Simpler Example
##

# Simplified from 

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

t = np.linspace(0, 3, 400)
g = -9.81
v02 = 5
z2 = g * t**2 / 2 + v02 * t

fig, ax = plt.subplots()

line2 = ax.plot(t[0], z2[0], label=f'v0 = {v02} m/s')[0]
ax.set(xlim=[-1, 4], ylim=[-30, 3], xlabel='Time [s]', ylabel='Z [m]')
ax.legend()

def update(frame):
    # update the line plot:
    line2.set_xdata(t[:frame])
    line2.set_ydata(z2[:frame])
    return line2


ani = animation.FuncAnimation(fig=fig, func=update, frames=400, interval=30)
plt.show()
ani.save('animation.mp4')
