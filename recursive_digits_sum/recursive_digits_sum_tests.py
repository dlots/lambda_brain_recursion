import unittest
from recursive_digits_sum import recursive_digits_sum


class TestRecursiveDigitsSum(unittest.TestCase):
    def test_recursive_digits_sum(self):
        for number in range(999999):
            true_sum = sum([int(digit) for digit in str(number)])
            self.assertEqual(recursive_digits_sum(number), true_sum)


if __name__ == '__main__':
    unittest.main()
