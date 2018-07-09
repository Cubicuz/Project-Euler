##If we take 47, reverse and add, 47 + 74 = 121, which is palindromic.
##
##Not all numbers produce palindromes so quickly. For example,
##
##349 + 943 = 1292,
##1292 + 2921 = 4213
##4213 + 3124 = 7337
##
##That is, 349 took three iterations to arrive at a palindrome.
##
##Although no one has proved it yet, it is thought that some numbers, like 196, never produce a palindrome.
##A number that never forms a palindrome through the reverse and add process is called a Lychrel number.
##Due to the theoretical nature of these numbers, and for the purpose of this problem,
##we shall assume that a number is Lychrel until proven otherwise. In addition you are given that for every
##number below ten-thousand, it will either (i) become a palindrome in less than fifty iterations, or,
##(ii) no one, with all the computing power that exists, has managed so far to map it to a palindrome.
##In fact, 10677 is the first number to be shown to require over fifty iterations before producing a
##palindrome: 4668731596684224866951378664 (53 iterations, 28-digits).
##
##Surprisingly, there are palindromic numbers that are themselves Lychrel numbers; the first example is 4994.
##
##How many Lychrel numbers are there below ten-thousand?
##
##NOTE: Wording was modified slightly on 24 April 2007 to emphasise the theoretical nature of Lychrel numbers.

##NOTE to self, might have been easier to just check the palindroms

maximumIterations = 50
initialValue = maximumIterations + 10
summOfLychrelNumbers = 0

## returns the reversed number
def reverse(number):
    retNumbr=0
    while number:
        retNumbr *=10
        retNumbr += number%10
        #remove last digit
        number //=10
    return retNumbr

#test reverse
#print(reverse(123456789))

## if number is palindrom returns 1
def isPalindrom(number):
    if number == reverse(number):
        return 1
    return 0

#use cashing to calculate every number only once
allNumbers = {}
for i in range(1, 10001):
    allNumbers[i]=initialValue


def recoursiveTest(number, recoursionDepth):
    if allNumbers[number] == maximumIterations:
        return maximumIterations
    if allNumbers[number] < maximumIterations:
        return allNumbers[number]+1
    

    reverseNumbr = reverse(number)
    
    #termination
    if recoursionDepth > 0 and reverseNumbr == number:
        return 0
    elif recoursionDepth >= maximumIterations:
        return maximumIterations

    newNumber = number + reverseNumbr

    if newNumber > 10000 and (not (newNumber in allNumbers)):
        allNumbers[newNumber] = initialValue
        
    iterations = recoursiveTest(newNumber, recoursionDepth+1)
    
    allNumbers[number] = iterations
    allNumbers[reverseNumbr] = iterations
    if iterations < maximumIterations:
        return iterations+1
    return maximumIterations

def main():
    summOfLychrelNumbers = 0 
    for i in range(1, 10001):
        recTest = recoursiveTest(i, 0) 
        if (recTest >= maximumIterations):
            summOfLychrelNumbers += 1
            print(i, recTest)
            
    print(summOfLychrelNumbers)
    
    
main()
print("done")
        
