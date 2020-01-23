
class PrimeHandling:

    def __init__(self):
        self.primeSet = set([1, 2, 3, 5, 7])
        self.primeList = list([1, 2, 3, 5, 7])
        self.maxTestedNumber = 9

    def isPrime(self, n):
        if n > self.maxTestedNumber:
            self.generatePrimesTo(n)
        return n in self.primeSet

    def _isPrime(self, n):
        for prime in self.primeList:
            if prime > 1:
                if n % prime == 0:
                    return False
            if prime > ((n**0.5) + 1) :
                return True

    def generatePrimesTo(self, n):
        for i in range(self.maxTestedNumber, n+1, 2):
            if self._isPrime(i):
                self.primeSet.add(i)
                self.primeList.append(i)
        self.maxTestedNumber = n
        

something = PrimeHandling()
assert(something.isPrime(5))
assert(something.isPrime(7))
assert(something.isPrime(11))
assert(something.isPrime(13))
assert(something.isPrime(17))
assert(not something.isPrime(21))
assert(not something.isPrime(25))
assert(not something.isPrime(27))
assert(not something.isPrime(51))
assert(not something.isPrime(9))
assert(not something.isPrime(15))
print(something.maxTestedNumber)
