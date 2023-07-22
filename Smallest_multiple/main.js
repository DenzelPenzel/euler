/*
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to n?
*/


// The smallest positive number that is evenly divisible by all of the numbers from 1 to n 
// is known as the least common multiple (LCM) 
function smallestMult(n) {
    let res = 1
    for (let i = 1; i < n + 1; i++) {
        res = lcm(res, i)
    }
    return res
}

// Least Common Multiple (LCM)
// smallest positive integer that is divisible by both a and b 
function lcm(a, b) {
    return Math.floor(Math.abs(a * b) / gcd(a, b))
}

// Greatest Common Divisor (GCD) 
// largest positive integer that divides each of the integers without leaving a remainder
function gcd(a, b) {
    while (b > 0) {
        [a, b] = [b, a % b]
    }
    return a
}


console.log(smallestMult(10))

