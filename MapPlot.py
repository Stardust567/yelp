import pandas as pd
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from matplotlib import animation

df = pd.read_csv('data/dataMap.csv', engine='python')
fig = plt.figure()
ax = fig.gca(projection='3d')
x = df['latitude']
y = df['longitude']

def init():
    # Plot the surface.
    ax.scatter(x, y, 0, zdir='z')
    ax.bar3d(x, y, 0, 0.0015, 0.0015, df['pos'], color='b', zsort='average')
    ax.bar3d(x, y, 0, 0.0015, 0.0015, -1 * df['neg'], color='r', zsort='average')
    return fig,

def animate(i):
    # azimuth angle : 0 deg to 360 deg
    ax.view_init(elev=10, azim=i*4)
    return fig,

ani = animation.FuncAnimation(fig, animate, init_func=init,repeat_delay=10,
                              frames=90, interval=50, blit=True)

ax.set_xlim(30.2, 30.4)
ax.set_ylim(-97.8, -97.65)
ax.set_zlim(-1*(df['neg'].max()), df['pos'].max())

fn = 'rotate_azimuth_angle_3d_surf'
ani.save(fn+'.mp4',writer='ffmpeg', fps=1000/50)
'''
surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)
# Customize the z axis.
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
# Add a color bar which maps values to colors.
fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()

ax.plot_surface(X, Y, Z, rstride=8, cstride=8, alpha=0.3)
cset = ax.contour(X, Y, Z, zdir='z', offset=-100, cmap=cm.coolwarm)
cset = ax.contour(X, Y, Z, zdir='x', offset=-40, cmap=cm.coolwarm)
cset = ax.contour(X, Y, Z, zdir='y', offset=40, cmap=cm.coolwarm)



ax.set_xticks([])
ax.set_yticks([])
#ax.set_zlim(-100, 100)


plt.show()'''