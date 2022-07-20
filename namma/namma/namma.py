import math
from matplotlib import pyplot
import numpy as np

def nsf(base, step):
    n = np.ceil(np.divide(base/step))
    m = np.divide(base/step)
    return np.prod(np.power(step,n),nsf1(m))

#NSF of step 1
def nsf1(base):
    temp = base
    num = 1.0
    while(temp>0):
        num=np.prod(num*temp)
        temp-=1
    return num

def nsf2(base):
    if base%1<0.01:
        num = math.gamma(base+1)
    else:
        num = math.gamma(base+1) * (base%1)
    return num

def main():
    nsfarr = []
    nsfarr2 = []
    gammaarr = []
    basearr = []
    newarr = []
    sinarr = []
    basearr=np.arange(0.00,5.00,0.01)
    for x in basearr:
        nsfarr.append(nsf1(x))
        ##nsfarr2.append(nsf2(x))
        gammaarr.append(math.gamma(x+1))
        #s = math.sin(x*math.pi/2)
        #sinarr.append(s)
    ##pyplot.plot(basearr,gammaarr, label = "Gamma(x+1)", linewidth=5)
    ##pyplot.plot(basearr,nsfarr, label = "NSF(x,1)", linewidth=5, alpha=0.6)

    #pyplot.plot(basearr,nsfarr2, label= "nsf2")
    #pyplot.plot(basearr,sinarr, label= "sin")

    #pyplot.xlabel("x")

    for y in range(0,len(basearr)):
        n = nsfarr[y]/gammaarr[y]
        s = 1.35*math.sin((y+math.pi)/120 - math.pi/120)
        sinarr.append(s)
        newarr.append(n)
    pyplot.plot(basearr,newarr, label="g(x)", linewidth=5)
    pyplot.axis(True)
    pyplot.title("g(x)")
    pyplot.legend()
    pyplot.show()
    #pyplot.plot(basearr,sinarr)

    #pyplot.title("NSF/Gamma")
    #pyplot.show()
    #m = nsf1(0.5)/math.gamma(0.5)
    #print(m)


if __name__ == "__main__":
    main()