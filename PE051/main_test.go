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

func TestNextComb(t *testing.T) {
	comb := []int{0, 1, 2, 3, 4, 5}
	fmt.Println(comb)
	hasNext, comb1 := next_comb(comb, 6, 6)

	if !hasNext {
		t.Error("expected hasNext")
	}
	for hasNext {
		fmt.Println(comb1)
		hasNext, comb1 = next_comb(comb1, 6, 6)
	}
}

func TestStuff(t *testing.T) {
	comb := []int{3, 4, 5}
	for i := range comb {
		fmt.Println(i)
	}
}
