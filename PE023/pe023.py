#A perfect number is a number for which the sum of its proper divisors is exactly equal to the number.
#For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
#
#A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.
#
#As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24.
#By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.
#
#Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
import math

#calc all abundant numbers below 28123
abundantNumbrs=set()
maxRange = 28123
for i in range(12, maxRange):
    # find primfactors
    sumOfPrimeFactors = 1 #1 is always a prime factor
    for j in range(2,int(math.sqrt(i) + 1)):
        if (i/j)%1 == 0: #this is a prime factor
            sumOfPrimeFactors += j
            if j != i/j: # j is not sqrt of i
                sumOfPrimeFactors += i/j
    if sumOfPrimeFactors > i:
        abundantNumbrs.add(i)

# these numbers are below the smallest abundant sum number
finalSum = 1+2+3+4+5+6+7+8+9+10+11+12+13+14+15+16+17+18+19+20+21+22+23
#check every number between 24 and 28123 if it can be written as the sum of two ubundant numbrs
print ("checking")
for i in range(25, 28123):
    j=1
    boolterminator = 0
    while (j < (i/2+1)) and (boolterminator == 0):
        if (j in abundantNumbrs) and ((i-j) in abundantNumbrs):
            boolterminator = 1
        j+=1
    if boolterminator == 0:
        finalSum += i
print(finalSum)
#done
