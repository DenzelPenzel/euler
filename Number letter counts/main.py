"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five, 
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to given limit inclusive were written out in words, how many letters would be used?

Note: 
    Do not count spaces or hyphens. 
    For example, 342 (three hundred and forty-two) 
    contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. 
    The use of "and" when writing out numbers is in compliance with British usage.
"""

import unittest
proper = [
    0,
    len("one"),
    len("two"),
    len("three"),
    len("four"),
    len("five"),
    len("six"),
    len("seven"),
    len("eight"),
    len("nine"),
    len("ten"),
    len("eleven"),
    len("twelve"),
    len("thirteen"),
    len("fourteen"),
    len("fifteen"),
    len("sixteen"),
    len("seventeen"),
    len("eighteen"),
    len("nineteen")
]

tenth = [
    len("twenty"),
    len("thirty"),
    len("forty"),
    len("fifty"),
    len("sixty"),
    len("seventy"),
    len("eighty"),
    len("ninety")
]

# Returns the length of the numbers between 0 and 99
def below100(n: int) -> int:
    if n < 20:
        return proper[n]
    return tenth[n // 10 - 2] + proper[n % 10]


def number_len(n: int) -> int:
    if n < 100:
        return below100(n)
    res = 0
    second_num = (n // 100) % 10
    top_num = n // 1000
    rest_num = n % 100

    if n > 999:
        res += below100(top_num) + len("thousand")
    if second_num != 0:
        res += proper[second_num] + len("hundred")
    if rest_num != 0:
        res += len("and") + below100(rest_num)
    return res


def number_letter_counts(limit: int) -> int:
    return sum([number_len(num) for num in range(1, limit + 1)])


class Test_Number_Letter_Counts(unittest.TestCase):
    def test_number_letter_counts(self):
        got = number_letter_counts(10)
        self.assertTrue(isinstance(got, int))

        for input, want in [[5, 19], [150, 1903], [1000, 21124]]:
            got = number_letter_counts(input)
            self.assertEqual(got, want)


if __name__ == "__main__":
    unittest.main()
