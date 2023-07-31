"""
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence: 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. 
Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under the given limit, produces the longest chain?

Note: Once the chain starts the terms are allowed to go above limit.

Collatz Problem - is one of the most famous unsolved problems in mathematics. 
The conjecture asks whether repeating two simple arithmetic operations 
will eventually transform every positive integer into 1
"""


import unittest
import functools

def longest_collatz_sequence(limit: int) -> int:
    functools.lru_cache(None)
    def collatz_sequence_length(n: int) -> int:
        if n == 1: return 0
        
        if n in memo:
            return memo[n]

        next_n = n // 2 if n % 2 == 0 else 3 *n + 1
        res = 1 + collatz_sequence_length(next_n)
        memo[n] = res
        return memo[n]


    max_length = 0
    start_number = 0
    memo = {}

    for num in range(1, limit + 1):
        current_length = collatz_sequence_length(num)
        if current_length > max_length:
            max_length = current_length
            start_number = num
    return start_number


class Test_Longest_Collatz_Sequence(unittest.TestCase):
    def test_longest_collatz_sequence(self):
        got = longest_collatz_sequence(10)
        self.assertTrue(isinstance(got, int))
        
        for input, want in [[14, 9], [5847, 3711], [46500, 35655], [54512, 52527], [100000, 77031], [1000000, 837799]]:
            got = longest_collatz_sequence(input)
            self.assertEqual(got, want)


if __name__ == "__main__":
    unittest.main()
