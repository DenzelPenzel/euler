/*
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below n.
*/


function primeSummation(n) {
    let prime = new Uint8Array(n)
    prime[0] = prime[1] = 1
    let sum = 0

    for (let k = 2; k < n; k++) {
        if (prime[k] == 0) {
            sum += k
            for (let i = k * k; i <= n; i += k) {
                prime[i] = 1
            }
        }
    }

    return sum
}


console.log(primeSummation(2000000));
