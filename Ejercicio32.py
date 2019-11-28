import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
	
Onda = np.loadtxt("onda.dat")

fig = plt.figure(figsize=(17,4))	

time = np.linspace(0,6,np.shape(Onda)[0])
x = np.linspace(0.0, 1.0, np.shape(Onda)[1])
Time,X = np.meshgrid(time,x)	

ax = fig.add_subplot(132,projection="3d")
surf = ax.plot_surface(Time,X,Onda.T,cmap=cm.viridis,edgecolor='none')
plt.xlabel('Time(s)')
plt.ylabel('X(m)')

plt.subplot(1,3,3)
plt.plot(x,Onda[0,:],c='gold',label='T = 0s')
plt.plot(x,Onda[-1,:],c='midnightblue',label='T = 6s')
plt.grid()
plt.legend()
plt.xlabel('X(m)')
plt.ylabel('Y(m)')
plt.title("WAVE EQUATION")	

plt.subplot(1,3,1)
plt.imshow(Onda,extent=[0,1,6,0],aspect=0.16)
plt.colorbar()
plt.xlabel('X(m)')
plt.ylabel('Time(s)')
plt.title("Y(m)")

plt.savefig("onda.png")
