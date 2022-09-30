import unittest
from random import shuffle
from recursive_second_max import second_max


class TestRecursiveSecondMax(unittest.TestCase):
    def test_recursive_second_max(self):
        values = list(range(300))
        shuffle(values)
        values.append(299)
        self.assertEqual(second_max(values), 298)


if __name__ == '__main__':
    unittest.main()
