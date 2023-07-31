"""
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits n!
"""
import math
import unittest


def sum_factorial_digits(n: int) -> int:
    return sum(map(int, str(math.factorial(n))))


class Test_sum_factorial_digits(unittest.TestCase):
    def test_sum_factorial_digits(self):
        got = sum_factorial_digits(10)
        self.assertTrue(isinstance(got, int))

        for input, want in [[10, 27], [25, 72], [50, 216], [75, 432], [100, 648]]:
            got = sum_factorial_digits(input)
            self.assertEqual(got, want)


if __name__ == "__main__":
    unittest.main()
