import numpy as np
import matplotlib.pyplot as plt

Onda = np.loadtxt("onda.dat")*10**5

plt.figure(figsize=(19,4))

time = np.linspace(0,0.1,np.shape(Onda)[0])
x = np.linspace(0,1,np.shape(Onda)[1])

plt.subplot(1,3,1)
plt.imshow(Onda,extent=[0,6,0.1,0],aspect=50)
plt.colorbar()
plt.xlabel('X (m)')
plt.ylabel('Time (s)')
plt.title("Y (m) $x10^5$")

plt.subplot(1,3,3)

Onda1 = Onda[:,int((len(x)-1)/4)]

plt.plot(time,Onda1,c='g')
plt.grid()
plt.xlabel('Time (s)')
plt.ylabel('Y (m) $x10^5$')
plt.title("Onda, x = 0.25m")

plt.subplot(1,3,2)

dt = int((len(time))/9)
t = 0
col = 0 

for i in range(9):
    t += dt*0.0001
    col += dt
    Onda2 = Onda[col,:]

    plt.plot(x,Onda2,label='t = '+str(np.round(t,3)))
    
plt.grid()
plt.legend(loc=1)
plt.xlabel('X (m)')
plt.ylabel('Y (m) $x10^5$')
plt.title("WAVE EQUATION")

plt.savefig("onda.png")
