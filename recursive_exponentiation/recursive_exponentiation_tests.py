import unittest
from recursive_exponentiation import recursive_exponentiation


class TestRecursiveExponentiation(unittest.TestCase):
    def test_recursive_exponentiation(self):
        for base in range(100):
            for power in range(5):
                self.assertEqual(recursive_exponentiation(base, power), base ** power)


if __name__ == '__main__':
    unittest.main()
