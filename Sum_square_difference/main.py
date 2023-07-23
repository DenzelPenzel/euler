"""
The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers 
and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first n natural numbers and the square of the sum.
"""

import math
import unittest


def sum_square_difference(n: int) -> float:
    # square of the sum of the first `n` natural numbers
    square_sum = math.pow((n * (n + 1)) // 2, 2)
    # sum of the squares of the first `n` natural numbers
    sum_of_square = n*(n+1) * (2*n + 1) / 6
    return square_sum - sum_of_square


class Test_Sum_Square_Difference(unittest.TestCase):
    def test_sum_square_difference(self):
        got = sum_square_difference(10)
        for input, want in [[10, 2640.0], [20, 41230.0], [100, 25164150.0]]:
            got = sum_square_difference(input)
            self.assertEqual(got, want)


if __name__ == "__main__":
    unittest.main()
