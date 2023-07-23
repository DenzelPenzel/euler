/*
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the given number?
*/

function largestPrimeFactor(num) {
    let factors = []
    let i = 2
    while (i * i <= num) {
        if (num % i) {
            i++
        } else {
            num /= i
            factors.push(i)
        }
    }
    if (num > 1) {
        factors.push(num)
    }
    return Math.max(...factors)
}