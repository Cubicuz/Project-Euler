# 1+2+3+4+5+6+7+8+9 = 45 -> never prime
# 1+2+3+4+5+6+7+8 = 36 -> never prime
# start with 7654321 -> 5040 possibilities
import itertools

def isPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False

    return True

ziffern = [7,6,5,4,3,2,1]
numbers = []
# liste aller permutationen
perms = list(itertools.permutations(ziffern, 7))
for perm in perms:
    numbr = 0
    for index in range(7):
        numbr = numbr + (perm[index] * pow(10, index))
    numbers.append(numbr)
numbers.sort(reverse=True)
for numbr in numbers:
    if isPrime(numbr):
        print(numbr)
        break
print("done")


