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
#     if the pattern is by 8, you are done

# check pattern:
# least significant digit musst be equal
# then go digit by digit to most significant
# if digits are unequal first time store the one on the left and the right
# if digits are unequal again compair if both sides are equal to their stored ones
# build a regex of the match (123*56**89)
# if the regex is in the dict:
#     increment its key,
#     check if key == 8
# else store it with 2

