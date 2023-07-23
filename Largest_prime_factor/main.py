"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the given number?
"""

import unittest


# The prime factors list of integers
# greater than 1 that has no positive integer divisors other than 1 and itself
# Prime factorization process
def largest_prime_factor(num):
    factors = []
    i = 2
    while i * 2 <= num:
        if num % i:
            i += 1
        else:
            num //= i
            factors.append(i)
    if num > 1:
        factors.append(num)
    return max(factors)


class Test_LargestPrimeFactor(unittest.TestCase):
    def test_largest_prime_factor(self):
        got = largest_prime_factor(5)
        self.assertTrue(isinstance(got, int))
        for input, want in [[2, 2], [3, 3], [5, 5], [7, 7], [8, 2], [13195, 29], [600851475143, 6857]]:
            got = largest_prime_factor(input)
            self.assertEqual(got, want)


if __name__ == "__main__":
    unittest.main()
