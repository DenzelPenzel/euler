/*
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below n.
*/


function primeSummation(n) {
    let prime = [false, ...Array(n - 2).fill(true)]
    let k = 2

    while (k * k <= n) {
        if (prime[k - 1]) {
            for (let i = k * k; i <= n; i += k) {
                prime[i - 1] = false 
            }
        }
        k++
    }

    return prime.reduce((acc, x, i) => {
        return x ? acc + (i + 1) : acc
    }, 0)
}

