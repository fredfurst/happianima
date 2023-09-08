##
## Matplotlib Simpler Example
##

# Simplified from 

import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(0, 3, 40)
g = -9.81
v02 = 5
z2 = g * t**2 / 2 + v02 * t

fig, ax = plt.subplots()
line2 = ax.plot(t, z2, label=f'v0 = {v02} m/s')
ax.set(xlim=[0, 3], ylim=[-4, 10], xlabel='Time [s]', ylabel='Z [m]')
ax.legend()
plt.show()