function length(n) {
    let c = 1
    for (; n > 1; c++) {
        if (n % 2 === 0)
            n /= 2;
        else
            n = 3 * n + 1;
    }
    return c;
}

function longestCollatzSequence(n) {
    let max = 0, max_i = 0;

    for (let i = 1; i < n; i++) {
        let l = length(i);
        if (l > max) {
            max = l;
            max_i = i;
        }
    }
    return max_i;
}
