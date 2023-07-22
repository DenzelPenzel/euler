/*

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which, a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000. 
Find the product abc such that a + b + c = n

*/

// brute force Time O(N^2)
// a < b < c and a + b + c = n
// maximum possible a = (a < (n / 3 - 1)) and (b < (n / 2 - 1))
// more optimal solution https://www.xarg.org/puzzle/project-euler/problem-9/
function specialPythagoreanTriplet(n) {
    for (let a = 1; a < Math.floor(n / 3); a++) {
        for (let b = a + 1; b < Math.floor(n / 2); b++) {
            let c = n - a - b
            if (a * a + b * b == c * c) {
                return a * b * c
            }
        }
    }
}



