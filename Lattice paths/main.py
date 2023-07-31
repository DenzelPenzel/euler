"""
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, 

there are exactly 6 routes to the bottom right corner.

a diagram of 6 2 by 2 grids showing all the routes to the bottom right corner

How many such routes are there through a given gridSize?

"""

import unittest
import math


def lattice_paths(n: int) -> int:
    # we can use the formula for calculating binomial coefficients
    return math.comb(n + n, n)


class Test_Lattice_Paths(unittest.TestCase):
    def test_lattice_paths(self):
        got = lattice_paths(4)
        self.assertTrue(isinstance(got, int))

        for input, want in [[4, 70], [9, 48620], [20, 137846528820]]:
            got = lattice_paths(input)
            self.assertEqual(got, want)


if __name__ == "__main__":
    unittest.main()
