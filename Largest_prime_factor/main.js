/*
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the given number?
*/

// The prime factors - list of integers 
// greater than 1 that has no positive integer divisors other than 1 and itself
// Prime factorization process
function largestPrimeFactor(n) {
    let d = 2
    let res = []
    
    while (n > 1) {
        while (n % d == 0) {
            res.push(d)
            n /= d
        }
        d += 1
    }

    return Math.max(...res)
}

console.log(largestPrimeFactor(20))

