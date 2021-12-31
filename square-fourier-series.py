import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as ss
from scipy.integrate import quad
import math as m
t=np.linspace(-5,+5,1000) 
y=ss.square(t) 
fc=lambda t:ss.square(t)*m.cos(i*t)  
fs=lambda t:ss.square(t)*m.sin(i*t)
n=50
An=[] 
Bn=[]
sum=0

for i in range(n):
    an=quad(fc,-np.pi,np.pi)[0]*(1.0/np.pi)
    An.append(an)

for i in range(n):
    bn=quad(fs,-np.pi,np.pi)[0]*(1.0/np.pi)
    Bn.append(bn) 

for i in range(n):
    if i==0.0:
        sum=sum+An[i]/2
    else:
        sum=sum+(An[i]*np.cos(i*t)+Bn[i]*np.sin(i*t))

plt.plot(t,sum,'g')
plt.plot(t,y,'r--')
plt.title("Fourier-Reihe für Rechteck")
plt.show()