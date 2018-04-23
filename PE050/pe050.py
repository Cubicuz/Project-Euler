#The prime 41, can be written as the sum of six consecutive primes:
#41 = 2 + 3 + 5 + 7 + 11 + 13
#
#This is the longest sum of consecutive primes that adds to a prime below one-hundred.
#
#The longest sum of consecutive primes below one-thousand that adds to a prime,
#contains 21 terms, and is equal to 953.
#
#Which prime, below one-million, can be written as the sum of the most consecutive primes?

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

mostConsecutivePrime = 0
mostConsecutiveCount = 0
for i in range(len(primNumbrs)-1):
    summ = 0
    #minimum length
    numberOfPrims = 21
    j = i
    while summ < primNumbrs[len(primNumbrs)-1]:
        summ += primNumbrs[j]
        if summ in primsSet:
            if mostConsecutiveCount < j - i:
                mostConsecutiveCount = j-i
                mostConsecutivePrime = summ
        j+=1
print(mostConsecutivePrime)
print(mostConsecutiveCount)
print("done")
    
    
#done
