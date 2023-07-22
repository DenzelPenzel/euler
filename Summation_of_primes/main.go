/*
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below n.
*/

package primes_sum

func PrimeSummation(n int) int {
	prime := make([]bool, n-1)
	k := 2

	for i := 1; i < n-1; i++ {
		prime[i] = true
	}

	for k*k <= n {
		if prime[k-1] {
			for i := k * k; i < n; i += k {
				prime[i-1] = false
			}
		}
		k++
	}

	res := 0

	for i, v := range prime {
		if v {
			res += i + 1
		}
	}

	return res
}
