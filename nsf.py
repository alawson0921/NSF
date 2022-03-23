#File: nsf.py (n-step factorials)
#Author: Adam Lawson
import math
import numpy as np
#from matplotlib import pyplot
#import numpy as np
##ADVICE: please keep the steps within [1,0.001) or maybe even [1,0.005)
##WE CAN TRY TO TEST WITH N>1...
#   note: 1.1 would be fine to work with so far

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
    print(f"{c} = {base}! with n-step of {nstep}")
    return c
###nsf raw
def nsfraw(nstep,base):
    b = base-nstep
    c = base
    while(b>0):
        c = c * b
        b = b-nstep
    return c
def long_nsfraw(nstep,base):
    b = long(base-nstep)
    c = long(base)
    while(b>0):
        c = c * b
        b = b-nstep
    return c
"""
#n-step factorial calculation
base1 = 3.0
num1 = nsf(0.5,base1)
print(f"{fact(base1)/num1} = factorial / n-step")
print(f"{num1/fact(base1)} = n-step / factorial")

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
"""
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
    print(f"The nsf equivalent is approximately {n:.15f}!({nsf_two_nstep})")
"""
##testing around some reverse_nsf's
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
print()
print(f"1.0!(0.5) + 2.0!(0.5) = n!(0.5)")
reverse_nsf((nsfraw(0.5,1.0)+nsfraw(0.5,2.0)),0.5)
##This should work with any two nsf's

##PROVE a!(x) + b!(y) = c!(z)
# EZ CLAP
# let's use 2!(0.5) + 2!(0.3) = n!(0.7)
print()
print(f"2.0!(0.5) + 2.0!(0.3) = n!(0.7)")
reverse_nsf((nsfraw(0.5,2.0)+nsfraw(0.3,2.0)),0.7)
print()
print()
##NOW I want to prove 2!(0.3) + 2!(0.5) = 2!(n)
    # very likely possible because the local minimum of 2 should be less than the sum
"""

"""
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

# FINDING THE MINIMUM (LOCAL)
def localmin(base):
    return 0.5 * base

functionmin = 0

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

nsf(0.0001,1.3997036774559777) ##THE BORDER! Still could go on forever
print()
print()
"""
lawson_const = 1.3997036774559777
"""
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
##x = np.arange(0,1,0.05)
##y = np.nsfraw(lawson_const,x)
##pyplot.plot(x,y)

##minimum finding function
def min(ns):
    if(ns<=lawson_const):
        return 0.0
    else:
        return 1.0

num = nsfraw(0.3,2) + nsfraw(0.5,2)
print(num)
##HOW CAN I GRAPH THIS? kekw
"""