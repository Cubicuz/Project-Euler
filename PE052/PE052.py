#It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.
#Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.

# first two digits musst be < 17

def digitOccurence(number):
    digits = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}
    while number:
        digits[number%10]+=1
    
        number //= 10
    return digits
# test funtion
# print(digitOccurence(5))


def checkNumber(number):
    digits1 = digitOccurence(number)
    for j in range(2, 7):
        digitsj = digitOccurence(number*j)
        for i in range(10):
            if digits1[i] != digitsj[i]:
                return 0
    return 1
        

def main():
    lowerBound = 1
    upperBound = (lowerBound * 10) // 6 + 1
    didWeFindItJet = 0
    while didWeFindItJet==0:
        for i in range(lowerBound, upperBound):
            if checkNumber(i):
                didWeFindItJet = 1
                print("the searched number is ", i)
                return;
        lowerBound *= 10
        upperBound = (lowerBound * 10) // 6 + 1
        print("lowerbound: ", lowerBound, " upperbound: ", upperBound)
        
main()
