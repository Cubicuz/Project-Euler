def isPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False

    return True


numberOfPrimes = 0
totalNumbers = 1
position = 1
step = 2
sidelength = 1
while numberOfPrimes/totalNumbers > 0.1 or position < 49:
    for i in range(4):
        totalNumbers +=1
        position += step
        if isPrime(position):
            numberOfPrimes +=1
    step += 2
    sidelength +=2
print(sidelength)
print("done")
