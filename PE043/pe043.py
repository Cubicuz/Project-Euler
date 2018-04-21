#The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order,
# but it also has a rather interesting sub-string divisibility property.
#
#Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:
#
#    d2d3d4=406 is divisible by 2
#    d3d4d5=063 is divisible by 3
#    d4d5d6=635 is divisible by 5
#    d5d6d7=357 is divisible by 7
#    d6d7d8=572 is divisible by 11
#    d7d8d9=728 is divisible by 13
#    d8d9d10=289 is divisible by 17
#
#Find the sum of all 0 to 9 pandigital numbers with this property.

import itertools

allPandigitalNumbers = itertools.permutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
reducedPandigitalNumbers = []
for numbr in allPandigitalNumbers:
# reihenfolge der Checks aus performancegründen geändert

#    d3d4d5 divisible by 5
    if (numbr[5] != 5 and numbr[5] != 0):
        continue
#    d1d2d3 divisible by 2
    if numbr[3] % 2 != 0:
        continue
#    d2d3d4 divisible by 3
    if (numbr[2]+numbr[3]+numbr[4]) % 3 != 0:
        continue
#    d7d8d9 divisible by 17
    if (numbr[7]*100+numbr[8]*10+numbr[9]) % 17 != 0:
        continue
#    d6d7d8 divisible by 13
    if (numbr[6]*100+numbr[7]*10+numbr[8]) % 13 != 0:
        continue
#    d5d6d7 divisible by 11
    if (numbr[5]*100+numbr[6]*10+numbr[7]) % 11 != 0:
        continue
#    d4d5d6 divisible by 7
    if (numbr[4]*100+numbr[5]*10+numbr[6]) % 7 != 0:
        continue
    reducedPandigitalNumbers.append(numbr)
totalSum=0
for numbr in reducedPandigitalNumbers:
    for i in range(0, 10):
        totalSum += numbr[i] * (10**(9-i))
print(totalSum)
