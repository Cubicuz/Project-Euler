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
i = 15
cont = 1
consecutiveCounter=0
print("start while")
while cont==1 and i < 500:
    i +=1
#    print('i {}'.format(i))
    if i in primsSet:
        consecutiveCounter=0
        continue

    #calculate prime factors
    primeFactors = []
    for j in primNumbrs:
#        print("j {}".format(j))
        # wenn j > wurzel der Zahl können wir aufhören nach primfaktoren zu suchen
        if j > math.sqrt(i)+2:
            break

        potenz = 1
        while i%(j**potenz)==0:
            potenz +=1
        potenz-=1
        if potenz > 0:
            primeFactors.append(j**potenz)
            # wenn es jetzt schon mehr als 4 primfaktoren gibt können wir zurück in die große while
            if len(primeFactors) > 4:
                break

    #check prime factors
    if len(primeFactors) != 4:
        consecutiveCounter=0
        continue

    consecutiveCounter +=1
    if consecutiveCounter > 3:
        for nmbr in primeFactors:
            if nmbr in factn1:
                consecutiveCounter = 1
                break
            if nmbr in factn2:
                consecutiveCounter = 2
                break
            if nmbr in factn3:
                consecutiveCounter = 3
                break
        if consecutiveCounter > 3:
            #found it
            break #break aus großer while
    factn3 = factn2
    factn2 = factn1
    factn1 = primeFactors


    
    
print("done")
print('{} : {}'.format(i-3, primeFactors))
print('{} : {}'.format(i-3, factn1))
print('{} : {}'.format(i-3, factn2))
print('{} : {}'.format(i-3, factn3))
