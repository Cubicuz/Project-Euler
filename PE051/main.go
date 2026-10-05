package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"sort"
	"strconv"
	"strings"
)

// thoughts:
// the number of * musst be a multiple of three, otherwise queersum will be three
// the number musst contain at least three times 0, 1 or 2
// I search for such primes and check them

var primes []int
var indexOfLastPrime int

const minimumDigitsForPrime = 3

func main() {
	// do performance testing, count nanoseconds for all of this

	loadPrimes(primePath)

	fmt.Printf("primecount: %v\n", len(primes))

	for j := 1000; j < len(primes); j++ {
		if isInteresting(primes[j]) {
			if evaluateInterestingPrime(primes[j]) {
				fmt.Printf("%v\n", primes[j])
				return
			}
		}
	}
}

func CalcAndStorePrimes() {
	primes = make([]int, 100_000_000)
	primes[0] = 2
	indexOfLastPrime = 0
	i := 3
	for indexOfLastPrime < len(primes)-1 {
		isPrimeBuildCache(i)
		i += 2
	}
	storePrimes(primePath)

}

const primePath = "./primes.csv"

func storePrimes(path string) {
	file, err := os.OpenFile(path, os.O_CREATE|os.O_WRONLY, 0666)
	if err != nil {
		fmt.Println("cant open file")
		os.Exit(-1)
	}
	defer file.Close()
	j := 0
	for i := 0; i < len(primes)-1; i++ {
		file.WriteString(fmt.Sprint(primes[i]) + ",")
		j++
		if j > 1000 {
			file.WriteString("\n")
			j = 0
		}
	}
	file.WriteString(fmt.Sprint(primes[len(primes)-1]))

}

func loadPrimes(path string) {
	file, err := os.OpenFile(path, os.O_CREATE|os.O_RDONLY, 0666)
	if err != nil {
		fmt.Println("cant open file")
	}
	defer file.Close()
	scanner := bufio.NewScanner(file)
	//primes = make([]int, 0, 100_000_000)
	primes = make([]int, 0)

	for scanner.Scan() {
		line := strings.Split(scanner.Text(), ",")
		for l := range line {
			if line[l] != "" {
				n, err := strconv.Atoi(line[l])
				if err != nil {
					fmt.Printf("something is wrong with '%s' in the line '%s' ", scanner.Text(), line[l])
				} else {
					primes = append(primes, n)
				}
			}
		}
	}

	if err := scanner.Err(); err != nil {
		fmt.Println(err)
	}
}

// store this as csv
func isPrimeBuildCache(n int) bool {
	sqrt := math.Sqrt(float64(n))
	isPrime := true
	i := 0
	for primes[i] < int(sqrt) {
		if n%primes[i] == 0 {
			isPrime = false
			break
		}
		i++
	}
	if isPrime {
		indexOfLastPrime++
		if indexOfLastPrime < len(primes) {
			primes[indexOfLastPrime] = n
		} else {
			primes = append(primes, n)
		}
	}
	return isPrime
}

func isPrime(n int) bool {
	index := sort.SearchInts(primes, n)
	if index >= len(primes) {
		// calculate more primes
		i := primes[len(primes)-1]
		isNPrime := false
		for i < n {
			addedNewPrime := false
			for !addedNewPrime {
				i += 2
				addedNewPrime = isPrimeBuildCache(i)
				if i == n {
					isNPrime = addedNewPrime
				}
			}
		}
		return isNPrime
	}

	if primes[index] == n {
		return true
	}
	return false
}

func isInteresting(n int) bool {
	// least significant digit is not interesting
	n = n / 10
	digits := make([]int, 10)

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
func evaluateInterestingPrime(n int) bool {
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
			if iterateOverPossibleCombinations3(nBackup, nAsDigits, j) {
				return true
			}
		}
		if digits[j] >= 6 {
			if iterateOverPossibleCombinations6(nBackup, nAsDigits, j) {
				return true
			}
		}
	}
	return false
}

func iterateOverPossibleCombinations3(n int, nAsDigits []int, goldenDigit int) bool {
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
		if testPrimeWithPattern(n, goldenIndex, comb, goldenDigit, isPrime) {
			fmt.Printf("found %v\n", n) // do more permutations
			return true
		}
		hasNextCombo, comb = next_comb(comb, k, n1)
	}
	return false
}
func iterateOverPossibleCombinations6(n int, nAsDigits []int, goldenDigit int) bool {
	goldenIndex := make([]int, 0)
	for j := 1; j < len(nAsDigits); j++ {
		if nAsDigits[j] == goldenDigit {
			goldenIndex = append(goldenIndex, j)
		}
	}

	// iterate over the possible combinations

	comb := make([]int, 6)
	for i := range 6 {
		comb[i] = i
	}

	k := 6
	n1 := len(goldenIndex)
	hasNextCombo := true
	for hasNextCombo {
		if testPrimeWithPattern(n, goldenIndex, comb, goldenDigit, isPrime) {
			fmt.Printf("found %v\n", n) // do more permutations
			return true
		}
		hasNextCombo, comb = next_comb(comb, k, n1)
	}
	return false
}

func testPrimeWithPattern(n int, goldenIndex []int, comb []int, goldenDigit int, isPrime func(int) bool) bool {
	add := 0
	nOrig := n
	for i := range comb {
		add += shift(goldenIndex[comb[i]])
	}

	fails := goldenDigit
	i := goldenDigit
	for fails < 3 && i < 9 {
		n += add
		if !isPrime(n) {
			fails++
		}
		i++

	}
	if fails < 3 {
		n = nOrig
		fmt.Printf("fails %v pattern %v\nPrime: %v\n", fails, add, n)
		for i := goldenDigit; i < 9; i++ {
			n = n + add
			if isPrime(n) {
				fmt.Printf("Prime: %v\n", n)
			}
		}
	}
	return fails == 2
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
