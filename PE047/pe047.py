#The first two consecutive numbers to have two distinct prime factors are:
#
#14 = 2 × 7
#15 = 3 × 5
#
#The first three consecutive numbers to have three distinct prime factors are:

#644 = 2² × 7 × 23
#645 = 3 × 5 × 43
#646 = 2 × 17 × 19.
#
#Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?

import math

def multiply(iterable):
    total = 1
    for i in iterable:
        total*=i
    return total

inp=""
f = open("../stuff/prims below one million.txt","r")
for line in f:
    inp+=line
prims=inp.split()
primsSet = set()
primNumbrs = []
for nmbr in prims:
    primsSet.add(int(nmbr))
    primNumbrs.append(int(nmbr))
primsSet.remove(1)
primNumbrs.remove(1)
primNumbrs.sort()
factn1 = []
factn2 = []
factn3 = []
primeFactors = []
i = 15
cont = 1
consecutiveCounter=0
print("start while")
while cont==1 and i < 1000000:
    i +=1
#    print('i {}'.format(i))
    if i in primsSet:
        consecutiveCounter=0
        continue

    #calculate prime factors
    primeFactors = []
    for j in primNumbrs:
#        print("j {}".format(j))
        # größter möglicher primfaktor [2, 3, 5, i/(2*3*5)] 
        if j > i/30 + 1:
            break
        # more efficient
        if i%j == 0:
            primeFactors.append(j)
        if len(primeFactors) > 4:
            break
        #could be more efficient but this was for debugging
#        potenz = 1
#        while i%(j**potenz)==0:
#            potenz +=1
#        potenz-=1
#        if potenz > 0:
#            primeFactors.append(j**potenz)


    #check prime factors
    if len(primeFactors) != 4:
        consecutiveCounter=0
        continue

    consecutiveCounter +=1

    if len(primeFactors) > 9:
        print('{} : {} : {}'.format(i-3, primeFactors, multiply(primeFactors)))
    if consecutiveCounter > 3:
        #found it
        print("done")
        break #break aus großer while
    factn3 = factn2
    factn2 = factn1
    factn1 = primeFactors
# done


    


print('{} : {} : {}'.format(i-3, primeFactors, multiply(primeFactors)))
print('{} : {} : {}'.format(i-3, factn1, multiply(factn1)))
print('{} : {} : {}'.format(i-3, factn2, multiply(factn2)))
print('{} : {} : {}'.format(i-3, factn3, multiply(factn3)))
