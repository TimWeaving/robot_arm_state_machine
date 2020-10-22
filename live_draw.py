# UNUSED

import random
from itertools import count
import time
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits import mplot3d
from matplotlib.patches import Circle, PathPatch
from matplotlib.text import TextPath
from matplotlib.transforms import Affine2D
import mpl_toolkits.mplot3d.art3d as art3d

plt.style.use('fivethirtyeight')

x_values = []
y_values = []
z_values = []

x_list_values = [0,1,1,0]
y_list_values = [0,0,1,0]
z_list_values = [0,0,1,0]

index = count()


def animate(i):

    #x = next(index)
    #x_values.append(x_list_values[x])
    #y_values.append(y_list_values[x])
    #z_values.append(z_list_values[x])
    x_values.append(random.randint(0, 2))
    y_values.append(random.randint(0, 2))
    z_values.append(random.randint(0, 2))


    ax.plot3D(x_values, y_values, z_values, 'blue',linestyle='--')
          
    time.sleep(.1)

fig = plt.figure()
ax = plt.axes(projection='3d')    
ani = FuncAnimation(plt.gcf(), animate, 10)


plt.tight_layout()
plt.show()