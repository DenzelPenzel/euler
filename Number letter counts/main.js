// proper nouns
const proper = [
    0,
    "one".length,
    "two".length,
    "three".length,
    "four".length,
    "five".length,
    "six".length,
    "seven".length,
    "eight".length,
    "nine".length,
    "ten".length,
    "eleven".length,
    "twelve".length,
    "thirteen".length,
    "fourteen".length,
    "fifteen".length,
    "sixteen".length,
    "seventeen".length,
    "eighteen".length,
    "nineteen".length
]

// tenth prefixes
const tenth = [
    "twenty".length,
    "thirty".length,
    "forty".length,
    "fifty".length,
    "sixty".length,
    "seventy".length,
    "eighty".length,
    "ninety".length
]

// Returns the length of the numbers between 0 and 99
function below100(n) {
    if (n < 20) {
        return proper[n]
    }
    return tenth[n / 10 - 2 | 0] + proper[n % 10]
}

function numberLength(n) {
    if (n < 100) {
        return below100(n)
    }

    let res = 0;
    let h = Math.floor(n / 100) % 10
    let t = Math.floor(n / 1000)
    let s = n % 100

    if (n > 999) {
        res += below100(t) + "thousand".length
    }
    if (h !== 0) {
        res += proper[h] + "hundred".length
    }
    if (s !== 0) {
        res += "and".length + below100(s)
    }
    return res
}

function numberLetterCounts(limit) {
    let res = 0
    for (let i = 1; i <= limit; i++) {
        res += numberLength(i)
    }
    return res
}
