package main

import (
	"fmt"
	"math"
)

// thoughts:
// the number of * musst be a multiple of three, otherwise queersum will be three
// the number musst contain at least three times 0, 1 or 2
// I search for such primes and check them

var primes []uint64
var indexOfLastPrime uint64

const minimumDigitsForPrime = 3

func main() {
	primes = make([]uint64, 10_000_000)
	primes[0] = 2
	indexOfLastPrime = 0
	numberOfInterestingPrimes := 0
	var i uint64
	for i = 3; i < 150_000_000; i += 2 {
		if isPrime(i, true) && i > 10000 && isInteresting(i) {
			numberOfInterestingPrimes++
		}
	}
	fmt.Printf("primecount: %v\n", indexOfLastPrime+1)
	fmt.Printf("interestingCount: %v\n", numberOfInterestingPrimes)

	for j := 1000; j < len(primes); j++ {
		if isInteresting(primes[j]) {
			if evaluateInterestingPrime(primes[j]) {
				fmt.Printf("%v\n", primes[j])
				return
			}
		}
	}
}

func isPrime(n uint64, add bool) bool {
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
	if isPrime && add {
		indexOfLastPrime++
		primes[indexOfLastPrime] = n
	}
	return isPrime
}

func isInteresting(n uint64) bool {
	// last digit is not interesting
	n = n / 10
	digits := make([]uint64, 10)

	for n > 0 {
		digit := n % 10
		digits[digit]++
		if digit < 3 && digits[digit] >= minimumDigitsForPrime {
			return true
		}
		n = n / 10
	}
	return false
}

// this function has to be refactored
func evaluateInterestingPrime(n uint64) bool {
	digits := make([]int, 10)
	nAsDigits := make([]int, 0)
	nBackup := n
	goldenDigits := []int{}
	nAsDigits = append(nAsDigits, int(n%10))
	n = n / 10
	for n > 0 {
		digit := int(n % 10)
		nAsDigits = append(nAsDigits, digit)
		digits[digit]++
		if digit < 3 && digits[digit] >= minimumDigitsForPrime { // could happen multiple times
			goldenDigits = append(goldenDigits, digit)
		}
		n = n / 10
	}
	for j := range 3 {
		if digits[j] >= minimumDigitsForPrime {
			if iterateOverPossibleIterations(nBackup, nAsDigits, j) {
				return true
			}
		}
	}
	return false
}

func iterateOverPossibleIterations(n uint64, nAsDigits []int, goldenDigit int) bool {
	goldenIndex := make([]int, 0)
	for j := 1; j < len(nAsDigits); j++ {
		if nAsDigits[j] == goldenDigit {
			goldenIndex = append(goldenIndex, j)
		}
	}

	// iterate over the possible combinations

	comb := make([]int, minimumDigitsForPrime)
	for i := range minimumDigitsForPrime {
		comb[i] = i
	}

	k := minimumDigitsForPrime
	n1 := len(goldenIndex)
	hasNextCombo := true
	for hasNextCombo {
		if testIndexes(n, goldenIndex, comb, goldenDigit) {
			fmt.Printf("meh %v\n", n) // do more permutations
			return true
		}
		hasNextCombo, comb = next_comb(comb, k, n1)
	}
	return false
}

func testIndexes(n uint64, goldenIndex []int, comb []int, goldenDigit int) bool {
	add := uint64(0)

	for i := range comb {
		add += uint64(shift(goldenIndex[comb[i]]))
	}

	fails := goldenDigit
	for fails < 4 {
		n += add
		if !isPrime(n, false) {
			fails++
		}

	}
	return fails < 4
}

func shift(i int) int {
	result := 1
	for j := 0; j < i; j++ {
		result *= 10
	}
	return result
}

func next_comb(comb []int, k int, n int) (bool, []int) {
	i := k - 1
	comb[i]++
	for (i > 0) && (comb[i] >= n-k+1+i) {
		i--
		comb[i]++
	}

	if comb[0] > n-k {
		return false, nil
	}

	for i = i + 1; i < k; i++ {
		comb[i] = comb[i-1] + 1
	}
	return true, comb
}
