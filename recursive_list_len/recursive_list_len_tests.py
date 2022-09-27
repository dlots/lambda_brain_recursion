import unittest
from recursive_list_len import recursive_list_len


class TestRecursiveListLen(unittest.TestCase):
    def test_recursive_list_len(self):
        for i in range(950):
            list_ = [0 for _ in range(i)]
            self.assertEqual(len(list_), recursive_list_len(list_))


if __name__ == '__main__':
    unittest.main()
