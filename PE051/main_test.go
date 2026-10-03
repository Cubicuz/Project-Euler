package main

import (
	"fmt"
	"testing"
)

func expectInteresting(t *testing.T, n uint64) {
	if !isInteresting(n) {
		t.Errorf("Expected interesting for %v", n)
	}
}
func expectBoring(t *testing.T, n uint64) {
	if isInteresting(n) {
		t.Errorf("Expected boring for %v", n)
	}
}

func TestIsInteresting(t *testing.T) {
	expectInteresting(t, 1111)
	expectInteresting(t, 2221)
	expectInteresting(t, 1020301)

	expectBoring(t, 1234)
	expectBoring(t, 112233004)
	expectBoring(t, 12301235554)
	expectBoring(t, 1234)
	expectBoring(t, 1234)
	expectBoring(t, 1234)
	expectBoring(t, 1234)
}

func compareCombination(calculated []int, expected []int, t *testing.T) {
	if len(calculated) != len(expected) {
		t.Errorf("Calculated (%v) and expected (%v) combination have different length\n calculated: %v\n expected: %v", len(calculated), len(expected), calculated, expected)
	}
}
func TestGenerationOfCombinations(t *testing.T) {
	n := 5
	k := 3
	comb := []int{}
	for i := range k {
		comb = append(comb, i)
	}
	fmt.Println(comb)

	expectedCombs := [][]int{
		{0, 1, 2},
		{0, 1, 3},
		{0, 1, 4},
		{0, 2, 3},
		{0, 2, 4},
		{0, 3, 4},
		{1, 2, 3},
		{1, 2, 4},
		{1, 3, 4},
		{2, 3, 4},
	}
	var hasNext bool
	for i := range expectedCombs {
		compareCombination(comb, expectedCombs[i], t)
		hasNext, comb = next_comb(comb, k, n)
		if i < len(expectedCombs)-1 && !hasNext {
			t.Error("expected to have next")
		}
	}
	if hasNext {
		t.Error("expected to not have next")
	}
}

func TestPatternGeneration(t *testing.T) {
	dummyIsPrimeN := []uint64{}
	dummyIsPrimeRetVal := true
	dummyIsPrime := func(n uint64) bool {
		dummyIsPrimeN = append(dummyIsPrimeN, n)
		return dummyIsPrimeRetVal
	}

	retval := testPrimeWithPattern(10100101, []int{1, 3, 4, 6}, []int{0, 1, 2}, 0, dummyIsPrime)

	expectedIsPrimeVals := []uint64{10111111, 10122121, 10133131, 10144141, 10155151, 10166161, 10177171, 10188181, 10199191}

	if !retval {
		t.Error("expected retval to be true")
	}

	for i := range expectedIsPrimeVals {
		if dummyIsPrimeN[i] != expectedIsPrimeVals[i] {
			t.Errorf("Function call to isPrime %v does not machexpected call with %v", dummyIsPrimeN[i], expectedIsPrimeVals[i])
		}
	}
}

func TestShifting(t *testing.T) {
	input := []int{0, 1, 2, 3, 10}
	expectedOutput := []uint64{1, 10, 100, 1000, 1_00000_00000}

	for i := range input {
		if shift(input[i]) != expectedOutput[i] {
			t.Errorf("input (%v) did not shift as expected (%v) but resulted in (%v)", input[i], expectedOutput[i], shift(input[i]))
		}
	}
}

func TestStuff(t *testing.T) {
	comb := []int{3, 4, 5}
	for i := range comb {
		fmt.Println(i)
	}
}
