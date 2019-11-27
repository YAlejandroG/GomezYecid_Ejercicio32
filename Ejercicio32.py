import os
import numpy as np
import matplotlib.pyplot as plt

difusion = np.loadtxt("difusion.dat")

xlab = [-1.0,-0.5,0.0,0.5,1.0]
tlab = [1.0,0.8,0.6,0.4,0.2,0.0]

plt.figure(figsize=(15,4))

time = difusion[:,0]
time = np.delete(time,-1)
x = difusion[-1,:]
x = np.delete(x,0)
Matrix = np.delete(difusion,0,1)
Matrix = np.delete(Matrix,-1,0)

plt.subplot(1,3,1)
plt.imshow(Matrix,extent=[-1,1,1,0],aspect=2.0)
plt.colorbar()
plt.xlabel('X (m)')
plt.ylabel('Time (s)')
plt.title("$\Psi$ ($m^2/s$)")

plt.subplot(1,3,3)

Psi1 = difusion[:,16]
Psi1 = np.delete(Psi1,-1)

plt.plot(time,Psi1,c='g')
plt.grid()
plt.xlabel('Time (s)')
plt.ylabel('$\Psi$ ($m^2/s$)')
plt.title("DIFUSION, x = 0m")

plt.subplot(1,3,2)

dt = int(len(time)/10)
col = 0 

for i in range(9):
    col += dt
    Psi2 = difusion[col,:]
    Psi2 = np.delete(Psi2,0)

    plt.plot(x,Psi2,alpha=(i+1)/9,color='k',label='t = '+str(difusion[col,0]))
    
plt.grid()
plt.legend(loc=1)
plt.xlabel('X (m)')
plt.ylabel('$\Psi$ ($m^2/s$)')
plt.title("DIFUSION")

plt.savefig("difusion.png")
