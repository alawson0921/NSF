#File: nsf.py (n-step factorials)
#Author: Adam Lawson
import math
from matplotlib import pyplot
import numpy as np
##ADVICE: please keep the steps within [1,0.001) or maybe even [1,0.005)
##WE CAN TRY TO TEST WITH N>1...
#   note: 1.1 would be fine to work with so far

#cleaned 3/2/2022

#normal factorial
def fact(j):
    return math.factorial(j) 
##NSTEP FACTORIAL FUNCTION
def nsf(nstep,base):
    b = base-nstep
    c = base
    while(b>0):
        c = c * b
        b = b-nstep
    print("{0} = {1}! with n-step of {2}".format(c,base,nstep))
    return c
###nsf raw
def nsfraw(nstep,base):
    b = base-nstep
    c = base
    while(b>0):
        c = c * b
        b = b-nstep
    return c

def nsftest1():
    #n-step factorial calculation
    base1 = 3.0
    num1 = nsf(0.5,base1)
    frac1 = fact(math.floor(base1/num1))
    frac2 = fact(math.floor(num1/base1))
    print("{0} = factorial / n-step".format(frac1))
    print("{0} = n-step / factorial".format(frac2))

    print()

    ##comparison with another n with the same a
    num2 = nsf(0.6,base1)
    print()

    ##comparison with another n with the same a pt 2
    num3 = nsf(0.4,base1)
    print()





    ####################################################################################################################

    ##HOW CAN WE FIND a! = b! with different n-factorial steps?
    #let's use 1!n=0.5 and try to find a b!n=0.25
    nsf(0.5,1.0)
    nsf(0.25,1.981330750601577)

##use nsfraw for nsf_one and limit 0.2 < nsf_two_step < 1.0
def reverse_nsf(nsf_one,nsf_two_nstep):
    n = 1.0
    inc = 1.0
    prev = 1.0
    inccount = 0
    g = nsf_one
    while(g - nsfraw(nsf_two_nstep,n) > 0.000000000000009*g or nsfraw(nsf_two_nstep,n) - g > 0.000000000000009*g):
         ##which decimal place
        if(nsfraw(nsf_two_nstep,n)<=g):
            prev = n
            if(inccount < 9):
              n = n + inc
              inccount+=1
            else:
                inc = inc / 10
                inccount = 0
        else:
            ##make the increments 0.1 times smaller
            ##revert n
            n = prev
            inc = inc / 10
            inccount = 0
    print("The nsf equivalent is approximately {0}!({1})".format(n,nsf_two_nstep))

##testing around some reverse_nsf's
def testrnsf1():
    reverse_nsf(nsfraw(0.5,1.0),0.25)
    reverse_nsf(nsfraw(0.3,4),0.2)
    print(nsfraw(0.2,3.368574678837455))
    print(nsfraw(0.3,4.0))
    reverse_nsf(nsfraw(1.1,math.e),0.9)
    print(math.e)
    nsf(0.01,math.e)




################################################################################################################

##CAN WE FIND a! + b! = c! with differnet and/or same n-factorial steps?
##YES: here's the proof
def testfltrnsf():
    print()
    print("1.0!(0.5) + 2.0!(0.5) = n!(0.5)")
    reverse_nsf((nsfraw(0.5,1.0)+nsfraw(0.5,2.0)),0.5)
##This should work with any two nsf's

##PROVE a!(x) + b!(y) = c!(z)
# EZ CLAP
# let's use 2!(0.5) + 2!(0.3) = n!(0.7)
    print()
    print("2.0!(0.5) + 2.0!(0.3) = n!(0.7)")
    reverse_nsf((nsfraw(0.5,2.0)+nsfraw(0.3,2.0)),0.7)
    print()
    print()


##NOW I want to prove 2!(0.3) + 2!(0.5) = 2!(n)
    # very likely possible because the local minimum of 2 should be less than the sum



################################################################################################################
##FIND A METHOD OF REVERSE NSF BUT WITH AN UNKNOWN N STEP INSTEAD OF BASE

# this is going to be a lot harder since from the first example, 3.0!(0.5) is greater than both 3!(0.4) and 3!(0.6)
# 1. We know there's a minimum in this function (but we don't know what it is yet... maybe just 0.5)
# 2. We also know that we may not be able to prove a!(x) = b!(y) where x does not equal to y because of this minimum
#       however there could be a solution in the negatives
# 3. However, finding the reverse nsf with a specific number above the minimum is possible with any a and n
# 4. There are restrictions when confined to a specific base(a) where there is a local minimum.
# 5. What we really know is that the range of this function from the domain of x>0 is the specific minimum (m), to infinity
# 6. We must find a way to find the local minimum with a fixed base(a) 


FUNCTIONMIN = 0

#Testing the limits of nsf. It does approach infinity on two sides
"""
nsf(0.1,1.0) ##smallest value with a=1.0, probably proving that the function nsf has a range of (0,inf)
nsf(0.2,1.0)
nsf(0.3,1.0)
nsf(0.4,1.0)
nsf(0.5,1.0)
nsf(0.6,1.0)
nsf(0.7,1.0)
nsf(0.8,1.0)
nsf(0.9,1.0)
print()
print()
nsf(0.1,2.0)
nsf(0.2,2.0) ##smallest value with a=2.0, could beat out second place
nsf(0.3,2.0) ##THIS GAP IS THE MOST INTERESTING BECAUSE it goes from [(0.1,10^-1),(0.2,10^-16),(0.3,10^-1),(0.4,10^-16),(0.5,10^1)]
nsf(0.4,2.0) ##pretty close second, might be able to go lower with more depth to the n-step (COULD BE LOCAL MIN AROUND HERE BECAUSE OF THE JUMP FROM 1.5 TO 10^-16)
nsf(0.5,2.0)
nsf(0.6,2.0)
nsf(0.7,2.0)
nsf(0.8,2.0)
nsf(0.9,2.0)
nsf(0.001,2.0) ###THIS IS THE MINIMUM at 0
print()
print()

##WHAT IS THE POINT AT WHICH n->0 switches between infinity and 0?
nsf(0.1,3.0)
nsf(0.01,3.0)
nsf(0.001,3.0) #reaches infinity
print()
print()

nsf(0.1,math.e)
nsf(0.01,math.e)
nsf(0.001,math.e) #also reaches inf
print()
print()

nsf(0.1,2.3)
nsf(0.01,2.3)
nsf(0.001,2.3) ##decreases
nsf(0.0001,2.3) ##reaches inf?
"""
##FOUND A CONSTANT IN A FUNCTION and more tests
"""
nsf(0.0001,1.3997036774559777) ##THE BORDER! Still could go on forever
print()
print()

lawson_const = 1.3997036774559777
##NEXT: How do we find the local minimum of a base > 1.399703774559777?
#find the number where the local minimum of that base does not decrease
nsf(0.1,4)
nsf(0.05,4)
nsf(0.01,4)
nsf(0.005,4)
print()
print()
##THIS IS INSANE!!!!
nsf(0.1,6)
nsf(0.05,5)
nsf(0.01,5)
nsf(0.005,5)
print()
print()
"""

lawson_const = 1.3997036774559777
#x = np.arange(0,1,0.01)

##array for y axis to plot
def myar(st,fin,base,step):
    ar = []
    i = float(st)
    if(i == 0):
        i = i + step
        if(base <= lawson_const):
            ar.append(0.00)
        else:
            ar.append(1000)
    while(i<=fin):
        if(nsfraw(i,base)>999):
            ar.append(1000)
        else:
            ar.append(nsfraw(i,base))
        i = i + step
    return ar

##array of points raw
def nsf_ar(st,fin,base,step):
    ar = []
    i = float(st)
    if(i == 0):
        i = i + step
        if(base <= lawson_const):
            ar.append(0.00)
        else:
            ar.append(99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999)
    while(i<=fin):
            ar.append(nsfraw(i,base))
            i = i + step
    return ar

##local maximum
def localmax(st,fin,base,step):
    ar = []
    if(base>lawson_const):
        return -1
    else:
        ar = nsf_ar(st,fin,base,step)
        ar.sort()
        return ar[ar.count()-1]

def graphnsf():
    y = myar(0,1,lawson_const,0.01)

    pyplot.plot(x,y)
    pyplot.title("NSF Lawson_constant!(x)")
    pyplot.show()

    x = np.arange(0,2,0.01)
    y = myar(0,2,lawson_const,0.01)

    pyplot.plot(x,y)
    pyplot.title("NSF Lawson_constant!(x)")
    pyplot.show()

    ##Another graph
    x2 = np.arange(0,2,0.01)

    y2 = myar(0,2,3,0.01)

    pyplot.plot(x2,y2)
    pyplot.title("NSF 3!(x)")
    pyplot.show()

    ##Another graph
    x3 = np.arange(0,2,0.01)
    y3 = myar(0,2,2,0.01)

    pyplot.plot(x3,y3)
    pyplot.title("NSF 2!(x)")
    pyplot.show()

    ##Another graph
    x4 = np.arange(0,2,0.01)
    y4 = myar(0,2,4,0.01)
    pyplot.plot(x4,y4)
    pyplot.title("NSF 4!(x)")
    pyplot.show()

    ##Another graph
    x5 = np.arange(0,2,0.01)
    y5 = myar(0,2,8,0.01)

    pyplot.plot(x5,y5)
    pyplot.title("NSF 8!(x)")
    pyplot.show()


##minimum finding function
def minnsf(ns,step_end):
    if(ns<=lawson_const):
        return 0.0
    else:
        ar = myar(0.01,step_end,ns,0.01)
        ar.sort()
        return ar[0]

##override twopoint
def decfind(num,base,p1,p2,mag,lim):
    while(mag>lim):
        ar = nsf_ar(p1,p2,num,mag)
        for i in range(0,len(ar)):
            if(ar[i]<=num and ar[i+1]>num): ##this is the flaw??
                p1 = ar[i]
                p2 = ar[i+1]
                return p1
        mag = mag/10
    return p1


#reverse nsf-n
def reversensf_n(num,base):
    p1 = 0
    p2 = 0
    mag = 0.01
    ans = 0.0
    lim = base * 0.0000000000009
    localmin = minnsf(base,2)
    if(num < localmin):
        print("Cannot find the reverse NSF: exceeds localmin")
    else:
        #decimal find
        if(localmax(0,num/2,base,0.01)==-1):
            print("There may be a solution really close to 0")
            if(num>base):
                return 0
            ##STEP 2: NUM < BASE continue with a set p1
            ##STEP 3: HOW TO SET P1?

        ##decimal method
        ##ans = decfind(num,base,p1,p2,mag,lim)
        ans = 0

        return ans
            ##WILL STRUGGLE WITH BIG NUMBERS

        ## 1. ALSO CREATE A LOCAL MAX with conditions of ignoring the infinity at n=0 first, then if it exceeds those, the answer
        ##       might be so close to 0 it cannot be calculated if the number is greater than the lawson const
        
        ## 2. CREATE AN APPROXIMATOR DECIMALLY if condition 1 holds in favor of the local max
        ## 3. DO NOT FORGET TO HAVE THE MAXNSF UPDATED WITH ITS OWN ARRAY

def rnsfn(num,base):
    lim = 0.01
    p1 = 0
    ans = 0.0
    localmin = minnsf(base,2)
    if(num < localmin):
        print("Cannot find the reverse NSF: exceeds localmin")
    else:
        #decimal find
        if(localmax(0,num/2,base,0.01)==-1):
            print("There may be a solution really close to 0")
            if(num>base):
                return 0
        ar = nsf_ar(0.1,2,base,0.01)
        for i in range(0,len(ar)):
            if(nsfraw(ar[i],base)-lim <num and nsfraw(ar[i],base)+lim > num):
                return ar[i]
        
##prove 2!(0.24) + 2!(0.49) = 2!(n)
print("2!(0.24) + 2!(0.49) = 2!(n)")
num = nsfraw(0.24,2) + nsfraw(0.49,2)
print("Finding {0}".format(num))
##ans = reversensf_n(num,2)


##testing method 2
ans = rnsfn(num,2)


print("n={0}".format(ans))
##ans approx = 0.64

#ANALYSIS: DIVERGING PLOT
def divergeplot():
    x = []
    y = []
    a = np.arange(lawson_const+0.01,10.0,0.01)
    #n!m
    for n in a:
        ar = nsf_ar(0.01,n/2,n,0.01)
        ar1 = ar
        ar.reverse()
        i = 0
        for m in ar:
            if m > 99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999:
                y.append(float(ar1.index(m)*0.01))
                x.append(n)
                break
            i+=1
    pyplot.plot(x,y)
    pyplot.title("Diverging x!y")
    pyplot.ylabel("Point of divergence x!y")
    pyplot.show()
    x1 = x[0]
    y1 = y[0]
    x2 = x[len(x)-1]
    y2 = y[len(y)-1]
    ##slope
    slope = (y2-y1)/(x2-x1)
    ##intersect
    b = y1 - (slope*x1)
    #print("y={0}x+{1}".format(slope,b))
    #answer y=0.4926470588235291x+0.013675394194481605
    x3 = b/(slope - 0.5)
    y3 = 0.5 * x3
    print("diverging and maximum at point ({0},{1})".format(x3,y3))

divergeplot()


def divergeplot2():
    x = []
    y = []
    a = np.arange(3,1000.0,1)
    #n!m
    for n in a:
        ar = nsf_ar(0.01,n/2,n,0.01)
        ar1 = ar
        ar.reverse()
        i = 0
        for m in ar:
            if m > 99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999:
                y.append(float(ar1.index(m)*0.01))
                x.append(n)
                break
            i+=1
    pyplot.plot(x,y)
    pyplot.title("Diverging x!y")
    pyplot.ylabel("Point of divergence x!y")
    pyplot.show()
    print(x[0])
    print(y[0])
    print(x[len(x)-1])
    print(y[len(y)-1])

#divergeplot2()

def findintersect():
    x = []
    y = []
    a = np.arange(lawson_const+0.01,10.0,0.01)
    #n!m
    for n in a:
        ar = nsf_ar(0.01,n/2,n,0.01)
        ar1 = ar
        ar.reverse()
        i = 0
        for m in ar:
            if m > 99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999:
                y.append(float(ar1.index(m)*0.01))
                x.append(n)
                break
            i+=1
    for yvalue in y:
        for xvalue in x:
            if(yvalue<xvalue/2.01 and yvalue>xvalue/2):
                print("x/2: {0}".format(xvalue))
                print("y: {0}".format(yvalue))

#findintersect()