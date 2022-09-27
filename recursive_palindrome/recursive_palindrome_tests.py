import unittest
from recursive_palindrome import recursive_palindrome


class TestPalindrome(unittest.TestCase):
    def test_check_palindrome(self):
        data = {
            "redivider": True,
            "deified": True,
            "civic": True,
            "radar": True,
            "python": False,
            "console": False,
            "qiopfghqujikfgbegbf": False
        }
        for string in data:
            self.assertEqual(recursive_palindrome(string), data[string])


if __name__ == '__main__':
    unittest.main()
