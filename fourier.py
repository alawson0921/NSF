import math
import numpy as np

def nsf(base, step):
    n = math.ceil(base/step)
    m = base/step
    return step**n * nsf1(m)

#nsf(step,1)
def nsf1(base):
    temp = base
    num = 1
    while(temp>0):
        num=num*temp
        temp-=1
    return num

def nsf2(base):
    if base%1<0.01:
        num = math.gamma(base+1)
    else:
        num = math.gamma(base+1) * (base%1)
    return num

def g(x):
    ans = nsf1(x)/math.gamma(x+1)
    return ans

def fourier():
    superlist = []
    alist = []
    blist = []
    clist = []
    dlist = []
    elist = []
    flist = []
    glist = []
    hlist = []
    ilist = []
    jlist = []
    for a in range(0,10):
        num = math.sin(0.1*(1+0.1*a))/math.sin(0.1)
        superlist.append(num)
    return superlist

def main():
    sl=fourier()
    print(sl)
    for b in range(1,21):
        print(g(1+0.05*b))

main()