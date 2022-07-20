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

def sines(x,y):
    return math.sin(x*y)

##input is the number of terms
def makematrix():
    ma = np.zeros((10,10))
    j = 1/10
    hx=np.arange(0.1,1.1,0.1)
    ###buggy so brute forcing
    ma1=[]
    ma2=[]
    ma3=[]
    ma4=[]
    ma5=[]
    ma6=[]
    ma7=[]
    ma8=[]
    ma9=[]
    ma10=[]

    for i in hx:
        s1=sines(0.1,i)
        s2=sines(0.2,i)
        s3=sines(0.3,i)
        s4=sines(0.4,i)
        s5=sines(0.5,i)
        s6=sines(0.6,i)
        s7=sines(0.7,i)
        s8=sines(0.8,i)
        s9=sines(0.9,i)
        s10=sines(1.,i)
        ma1.append(s1)
        ma2.append(s2)
        ma3.append(s3)
        ma4.append(s4)
        ma5.append(s5)
        ma6.append(s6)
        ma7.append(s7)
        ma8.append(s8)
        ma9.append(s9)
        ma10.append(s10)
    matrix = []
    matrix.append(ma1)
    matrix.append(ma2)
    matrix.append(ma3)
    matrix.append(ma4)
    matrix.append(ma5)
    matrix.append(ma6)
    matrix.append(ma7)
    matrix.append(ma8)
    matrix.append(ma9)
    matrix.append(ma10)

    return matrix

def gxmatrix():
    hx=np.arange(0.1,1.1,0.1)
    gxm=[]
    for i in hx:
        gxm.append(g(i))
    return gxm

def makefx(sol):
    num=sol[0]*sines(0.1,0.1)+sol[1]*sines(0.1,0.2)+sol[2]*sines(0.1,0.3)+sol[3]*sines(0.1,0.4)+sol[4]*sines(0.1,0.5)+sol[5]*sines(0.1,0.6)+sol[6]*sines(0.1,0.7)+sol[7]*sines(0.1,0.8)+sol[8]*sines(0.1,0.9)+sol[9]*sines(0.1,1.)
    return num

def main():
    soe = makematrix()
    gs = gxmatrix()
    sol = np.linalg.solve(soe,gs)
    print(sol)
    num = makefx(sol)
    print(num)
    print(g(0.1))

main()
