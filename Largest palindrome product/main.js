/*
A palindromic number reads the same both ways. 
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two n-digit numbers.
*/


function isPalindrome(x) {
    if (x < 0 || (x % 10 == 0 && x != 0)) {
        return false
    }
    let revX = 0

    while (x > revX) {
        let d = x % 10
        revX = revX * 10 + d
        x = Math.floor(x / 10)
    }
    return x == revX || Math.floor(revX / 10) == x
}

function largestPalindromeProduct(n) {
    const start = Math.pow(10, n - 1)
    const end = Math.pow(10, n)
    let res = 0
    for (let i = end - 1; i >= start; i--) {
        for (let j = end - 1; j >= start; j--) {
            if (isPalindrome(i * j)) {
                if (i * j > res) {
                    res = i * j
                }
            }
        }
    }

    return res
}

console.log(largestPalindromeProduct(3))