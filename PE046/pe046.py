# composite is the opposit of prime
#
#It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.
#
#9 = 7 + 2×1^2
#15 = 7 + 2×2^2
#21 = 3 + 2×3^2
#25 = 7 + 2×3^2
#27 = 19 + 2×2^2
#33 = 31 + 2×1^2
#
#It turns out that the conjecture was false.
#
#What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?

inp=""
f = open("../stuff/prims below one million.txt","r")
for line in f:
    inp+=line
prims=inp.split()
primsSet = set()
for prim in prims:
    primsSet.add(int(prim))
print("read")
cont = 1
i=13
while cont==1:
    i+=2
    if i in primsSet:
        continue
    j=1
    canBeWritten=0
    while (i-2*j*j > 0) and (canBeWritten==0):
        if (i-2*j*j in primsSet):
            canBeWritten = 1
        j+=1
    if canBeWritten == 0:
        cont = 0
        print('its this {}'.format(i))
#done        
