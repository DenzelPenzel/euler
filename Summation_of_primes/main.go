/*
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below n.
*/

package main

import (
	"fmt"
)

func primeSummation(n int) int {
	prime := make([]int, n+1)
	prime[0] = 1
	prime[1] = 1
	sum := 0

	for k := 2; k < n; k++ {
		if prime[k] == 0 {
			sum += k
			for i := k * k; i <= n; i += k {
				prime[i] = 1
			}
		}
	}

	return sum
}

func main() {
	for input, want := range map[int]int{17: 41, 2001: 277050, 140759: 873608362, 2000000: 142913828922} {
		got := primeSummation(input)
		if got != want {
			fmt.Printf("Test failed expect: %v, got: %v", want, got)
			break
		}
	}
	fmt.Println("OK")
}
