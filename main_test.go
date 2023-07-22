package main

import (
	"fmt"
	"testing"

	sp "github.com/denisschmidt/euler/Summation_of_primes"
	"github.com/stretchr/testify/require"
)

func SummationOfPrimes(t *testing.T) {
	for input, want := range map[int]int{17: 41, 2001: 277050, 140759: 873608362, 2000000: 142913828922} {
		fmt.Println(input, want)
		got := sp.PrimeSummation(input)
		require.Equal(t, got, want)
	}
}
