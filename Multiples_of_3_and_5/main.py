"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below the provided parameter value number.
"""

import unittest


def multiples_of_3_and_5(n: int) -> int:
    def sum_divisible_by(k: int) -> int:
        # calculates the number of multiples of `k`
        p = (n - 1) // k
        # calculates the sum of all the multiples of `k` less than `n`
        # it does this by using the formula for the sum of an arithmetic series
        # sum = n/2 * (first_term + last_term)
        # sum = p/2 * (k + p*k) => k * (p * (p + 1)) / 2
        return k * (p * (p + 1)) // 2

    # subtract sumDivisibleBy(15) avoid duplicates
    return sum_divisible_by(3) + sum_divisible_by(5) - sum_divisible_by(15)


class Test_Multiples_of_3_and_5(unittest.TestCase):
    def test_multiples_of_3_and_5(self):
        got = multiples_of_3_and_5(10)
        self.assertTrue(isinstance(got, int))
        for input, want in [[49, 543], [1000, 233168], [8456, 16687353], [19564, 89301183]]:
            got = multiples_of_3_and_5(input)
            self.assertEqual(got, want)


if __name__ == "__main__":
    unittest.main()
