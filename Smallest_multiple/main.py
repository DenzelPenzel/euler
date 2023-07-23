"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to n?
"""

import unittest

# Greatest Common Divisor (GCD)
# largest positive integer that divides each of the integers without leaving a remainder
def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


# Least Common Multiple (LCM)
# smallest positive integer that is divisible by both a and b
def lcm(a, b):
    return abs(a * b) // gcd(a, b)


# The smallest positive number that is evenly divisible by all of the numbers from 1 to n
# is known as the least common multiple (LCM)
def smallest_mult(n):
    res = 1
    for i in range(1, n + 1):
        res = lcm(res, i)
    return res


class Test_Smallest_Mult(unittest.TestCase):
    def test_smallest_mult(self):
        got = smallest_mult(10)
        self.assertTrue(isinstance(got, int))
        for input, want in [[5, 60], [7, 420], [10, 2520], [13, 360360], [20, 232792560]]:
            got = smallest_mult(input)
            self.assertEqual(got, want)


if __name__ == "__main__":
    unittest.main()
