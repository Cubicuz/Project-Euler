#Euler discovered the remarkable quadratic formula:
#
#n2+n+41
#
#It turns out that the formula will produce 40 primes for the consecutive integer values 0≤n≤39
#. However, when n=40,402+40+41=40(40+1)+41 is divisible by 41, and certainly when n=41,412+41+41
#
#is clearly divisible by 41.
#
#The incredible formula n2−79n+1601
#was discovered, which produces 80 primes for the consecutive values 0≤n≤79
#
#. The product of the coefficients, −79 and 1601, is −126479.
#
#Considering quadratics of the form:
#
#    n2+an+b
#
#, where |a|<1000 and |b|≤1000
#
#where |n|
#is the modulus/absolute value of n
#e.g. |11|=11 and |−4|=4
#Find the product of the coefficients, a
#and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n=0.

import math
maxprims=0
maxa=0
maxb=0
for a in range(-999,999,2):
    print(a)
    for b in range(-999,999,2):
        bol=0
        prims=0
        inc=0
        while bol==0:
            num=inc*inc+a*inc+b
            if num < 0:
                bol=1
            else:
                i = 2
                while i < math.sqrt(num)+1:
                    if (num/i)%1==0:
                        bol=1
                        i = num
                    i+=1
                        
                    
            inc+=1
        inc-=1
        if maxprims<inc:
            maxprims=inc
            maxa=a
            maxb=b

print(maxa,maxb,maxa*maxb)
