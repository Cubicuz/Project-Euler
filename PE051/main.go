package main

import (
	"fmt"
	"math"
)

var primes []uint64
var indexOfLastPrime uint64

func main() {
	primes = make([]uint64, 1_000_000)
	primes[0] = 2
	indexOfLastPrime = 0
	var i uint64
	for i = 3; i < 15_000_000; i += 2 {
		isPrime(i)
	}
	fmt.Printf("primecount: %v\n", indexOfLastPrime+1)
}

func isPrime(n uint64) bool {
	sqrt := math.Sqrt(float64(n))
	isPrime := true
	i := 0
	for primes[i] < uint64(sqrt) {
		if n%primes[i] == 0 {
			isPrime = false
			break
		}
		i++
	}
	if isPrime {
		indexOfLastPrime++
		primes[indexOfLastPrime] = n
	}
	return isPrime
}
