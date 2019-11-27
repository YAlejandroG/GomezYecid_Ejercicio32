import numpy as np
import matplotlib.pyplot as plt

Onda = np.loadtxt("onda.dat")

fig = plt.figure(figsize=(15,4))

time = np.linspace(0,6,np.shape(Onda)[0])
x = np.linspace(0.0, 1.0, np.shape(Onda)[1])
X, Time = np.meshgrid(x,time)

plt.subplot(1,3,1)
plt.imshow(Onda,extent=[0,1,6,0],aspect=2.0)
plt.colorbar()
plt.xlabel('X(m)')
plt.ylabel('Time(s)')
plt.title("Y(m)")

plt.subplot(1,3,2)
ax = plt.axes(projection='3d')
ax.contour3D(X,Time,Onda,cmap='Viridis')
ax.set_xlabel('X(m)')
ax.set_ylabel('Time(s)')
ax.set_title('Y(m)')

plt.subplot(1,3,3)
plt.plot(x,Onda[0,:],c='g',label='T = 0s')
plt.plot(x,Onda[-1,:],c='orange',label='T = 6s')
plt.grid()
plt.legend()
plt.xlabel('X(m)')
plt.ylabel('Y(m)')
plt.title("WAVE EQUATION")

plt.savefig("onda.png")
