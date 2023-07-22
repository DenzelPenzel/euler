/*
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the nth prime number?
*/

// Sieve of Eratosthenes
// An array of bits hi is used to mark primality, i.e. 
// mark[i] is True if i+1 is prime
// Eratosthenes -- ancient Greek mathematician
function nthPrime(n) {
    let limit = n > 6 ? 125000 : 16
    let prime = [false, ...Array(limit + 1).fill(true)]
    let k = 2
    while (k <= limit) {
        if (prime[k - 1]) {
            for (let i = k * k; i <= limit; i += k) {
                prime[i - 1] = false
            }
            n--
            if (n == 0) {
                return k
            }
        }
        k++
    }
    return -1
}

// This is a simple but not the most efficient implementation. 
// If you need to find large primes, there are more advanced algorithms 
// and even tables available online that could be faster
console.log(nthPrime(6))
