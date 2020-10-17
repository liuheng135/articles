import matplotlib.pyplot as plt 
import numpy as np 


x = np.linspace(0,np.pi * 40,2000)
s0 = np.sin(x)
x = np.linspace(0,np.pi * 2,2000)
s1 = np.sin(x)

sx = s0*s1

plt.plot(s0,'r')
plt.figure()
plt.plot(s1,'g')
plt.figure()
plt.plot(sx,'b')


r0 = np.zeros(4000)
r1 = np.zeros(4000)
r2 = np.zeros(4000)

for i in range(0,2000):
    r0[i+100]  = sx[i]
    r1[i+500]  = sx[i]
    r2[i+1000] = sx[i]

r0 *= 0.7
r1 *= 0.6
r2 *= 0.5

plt.figure()
plt.plot(r0,'r')
plt.plot(r1,'g')
plt.plot(r2,'b')

for i in range(0,4000):
    if r0[i] < 0 :
        r0[i] = 0
    if r1[i] < 0 :
        r1[i] = 0
    if r2[i] < 0 :
        r2[i] = 0
plt.figure()
plt.plot(r0,'r')
plt.plot(r1,'g')
plt.plot(r2,'b')

lost0 = 0.0
lost1 = 0.0
lost2 = 0.0
diff = 0.0

for i in range(0,4000):
    diff = r0[i] - lost0
    lost0 += diff * 0.0002
    r0[i] = lost0;

    diff = r1[i] - lost1
    lost1 +=  diff * 0.0002
    r1[i] = lost1;

    diff = r2[i] - lost2
    lost2 +=  diff * 0.0002
    r2[i] = lost2;

plt.figure()
plt.plot(r0,'r')
plt.plot(r1,'g')
plt.plot(r2,'b')    

plt.show()