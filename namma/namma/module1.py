import numpy as np
import matplotlib.pyplot as plt

def nsfn(base,step):
    temp = base
    nsfarr = []
    while temp < 0:
        nsfarr=np.append(nsfarr,temp)
        temp-=step
    return np.product(nsfarr)

def plotnsf():
    base = np.arange(-5.0,1.0,0.013,dtype=float)
    nsf = []
    for x in base:
        nsf=np.append(nsf,nsfn(x,-0.5))
    plt.scatter(base,nsf,label="NSF(x,1)")
    plt.legend()
    plt.show()

plotnsf()
