"""
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^exponent?
"""

import unittest
import math


def power_digit_sum(exponent: int) -> int:
    res = 2 ** exponent
    digit_sum = 0
    while res:
        digit_sum += res % 10
        res //= 10
    return digit_sum


class Test_Power_Digit_Sum(unittest.TestCase):
    def test_power_digit_sum(self):
        got = power_digit_sum(4)
        self.assertTrue(isinstance(got, int))

        for input, want in [[15, 26], [128, 166], [1000, 1366], [10000, 13561], [100000, 135178], [1000000, 1351546]]:
            got = power_digit_sum(input)
            self.assertEqual(got, want)


if __name__ == "__main__":
    unittest.main()
