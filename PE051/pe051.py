#By replacing the 1st digit of the 2-digit number *3,
#it turns out that six of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.
#
#By replacing the 3rd and 4th digits of 56**3 with the same digit,
#this 5-digit number is the first example having seven primes among the ten generated numbers,
#yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993. Consequently 56003,
#being the first member of this family, is the smallest prime with this property.
#
#Find the smallest prime which, by replacing part of the number
#(not necessarily adjacent digits) with the same digit, is part of an eight prime value family.


# thoughts:
# the last digit cant change because it needs to be odd

# find next prime
# store it in primes
# go down the stored primes and check if it fullfills the requirement with another prime
#     check their pattern and increment it
#     if the pattern is by 1+1+2+3+4+5+6+7, then there are 8 numbers
#     so 1+1+2+3+4+5+6+1 is sufficient (23)

# check pattern:
# least significant digit musst be equal
# then go digit by digit to most significant
# if digits are unequal first time store the one on the left and the right
# if digits are unequal again compair if both sides are equal to their stored ones
# build a regex of the match (123*56**89)
# if the regex is in the dict:
#     increment its key,
#     check if key == 8
# else store it with 1

import bisect

def getPattern(a, b):
    if (a%10 != b%10): # least significant digit musst be equal
        return None

    da = a % 10
    a = a // 10
    db = b % 10
    b = b // 10
    pattern = []
    differentNumbers = 0
    while True:
        if da == db:
            pattern.append(str(da))
        else:
            if differentNumbers == 0:
                differentNumbers = da*10 + db
            else:
                if differentNumbers != da*10 + db:
                    return None
            pattern.append("*")

        if a == 0:
            pattern.reverse()
            return "".join(pattern)

        da = a % 10
        a = a // 10
        db = b % 10
        b = b // 10

def getPatternSubtraction(a, b):
    diff = a - b
    while diff != 0:
        pass

    
def testGetPattern():
  print(getPattern(234277212, 234299212))
  print(getPattern(1331, 1221))
  print(getPattern(102121, 105151))
  print(getPattern(102121, 105151))
  print(getPattern(16661, 13631))
  print(getPattern(12221, 13341))
  
  exit()

#testGetPattern()
  

import math
prims = [2, 3, 5, 7]
primsLenIndex = []
def getNextPrime():
    isprim = False
    nextPrim = prims[-1]
    while not isprim:
        nextPrim += 2
        for prim in prims:
            if nextPrim % prim == 0:
                isprim = False
                break
            if prim > math.sqrt(nextPrim):
                isprim = True
                break
    prims.append(nextPrim)
    return nextPrim

def preparePrimes():
    prim = getNextPrime()
    for i in range(1, 7):
        while (prim < 10**i):
            prim = getNextPrime()
        primsLenIndex.append(len(prims)-1)

def testPreparePrimes():
    preparePrimes()
    print("Number of primes: ", len(prims))
    for i in primsLenIndex:
        print("Index: ", i)
        print("Prime bevore: ", prims[i-1])
        print("Prime after: ", prims[i])

#testPreparePrimes()
    
def isFinalPattern(pattern):
    cnt = 0
    for i in range(10):
        number = int(pattern.replace('*', str(i)))
        if number == prims[bisect.bisect_left(prims, number)]:
            cnt += 1
    if cnt >= 8:
        print(pattern, "saves the day")
        for i in range(10):
            number = int(pattern.replace('*', str(i)))
            if number in prims:
                print(number)
                return True
    return False
        

patterns = {}

def findGoldenPattern():

    for i in range(len(primsLenIndex)-1):
        for j in range(primsLenIndex[i], primsLenIndex[i+1]):
            #print(prims[j])
            if prims[j] > 300000:
                return ""
            for k in range(primsLenIndex[i], j):
                pattern = getPattern(prims[k], prims[j])
                if pattern is not None:
                    if pattern in patterns:
                        patterns[pattern] += 1
                        if patterns[pattern] == 4:
                            if pattern[0] == "*":
                                print("pattern", pattern)
                                if isFinalPattern(pattern):
                                    return pattern
                    else:
                        patterns[pattern] = 1


def main():
    preparePrimes()
    pattern = findGoldenPattern()

#main()
import cProfile
cProfile.run('main()')