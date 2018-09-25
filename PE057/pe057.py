

##
##    It is possible to show that the square root of two can be expressed as an infinite continued fraction.
##
##    √ 2 = 1 + 1/(2 + 1/(2 + 1/(2 + ... ))) = 1.414213...
##
##    By expanding this for the first four iterations, we get:
##
##    1 + 1/2 = 3/2 = 1.5
##    1 + 1/(2 + 1/2) = 7/5 = 1.4
##    1 + 1/(2 + 1/(2 + 1/2)) = 17/12 = 1.41666...
##    1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379...
##
##    The next three expansions are 99/70, 239/169, and 577/408, but the eighth expansion, 1393/985,
##    is the first example where the number of digits in the numerator exceeds the number of digits in the denominator.
##
##    In the first one-thousand expansions, how many fractions contain a numerator with more digits than denominator?
##

## nominator / denominator

## it seems to be denominator(n) = denominator(n-1)*2 + denominator(n-2)
## denominator(0) = 1
## denominator(1) = 2
## denominator(2) = 5
denominators = {}
for i in range(1001):
    denominators[i] = 0
denominators[0] = 1
denominators[1] = 2

def denominator(n):
    if denominators[n-1] == 0:
        # if n-1 is not calculated yet do it recoursively
        denominator[n-1]
        
    denominators[n] = denominators[n-1]*2 + denominators[n-2]
    return denominators[n]

## nominator: 3, 7, 17, 41, 99, 239, 577, 1393
## same as denominator with different starting points
## denominator(0) = 1
## denominator(1) = 3
## denominator(2) = 7

nominators = {}
for i in range(1001):
    nominators[i] = 0
nominators[0] = 1
nominators[1] = 3

def nominator(n):
    if nominators[n-1] == 0:
        # if n-1 is not calculated yet do it recoursively
        nominator[n-1]
        
    nominators[n] = nominators[n-1]*2 + nominators[n-2]
    return nominators[n]


def digitCount(number):
    summ = 0
    while number:
        summ += 1
        number //= 10
    return summ

totalRelevantFractions = 0

def main():
    global totalRelevantFractions
    for i in range(2, 1001):
        nomin = nominator(i)
        denomin = denominator(i)
        if digitCount(nomin) > digitCount(denomin):
            totalRelevantFractions += 1


main()
print(totalRelevantFractions)
        
