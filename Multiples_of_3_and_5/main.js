/*

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below the provided parameter value number.
*/


function multiplesOf3and5(n) {
    const sumDivisibleBy = (k) => {
        const p = Math.floor((n - 1) / k)
        return k * (p * (p + 1)) / 2
    }
    return sumDivisibleBy(3) + sumDivisibleBy(5) - sumDivisibleBy(15)
}