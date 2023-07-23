"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below n.
"""

import unittest


def prime_summation(n: int) -> int:
    prime = [0] * n
    prime[0] = prime[1] = 1
    summation = 0

    for k in range(2, n):
        if prime[k] == 0:
            summation += k
            for i in range(k * k, n, k):
                prime[i] = 1

    return summation


class Test_Prime_Summation(unittest.TestCase):
    def test_prime_summation(self):
        got = prime_summation(17)
        for input, want in [[17, 41], [2001, 277050], [140759, 873608362], [2000000, 142913828922]]:
            got = prime_summation(input)
            self.assertEqual(got, want)


if __name__ == "__main__":
    unittest.main()
