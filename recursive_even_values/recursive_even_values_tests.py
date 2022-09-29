import unittest
import io
import contextlib
import random
from recursive_even_values import print_even_values


class TestRecursiveEvenValues(unittest.TestCase):
    def test_recursive_even_values(self):
        high = 1000000
        in_values = list(range(high))
        random.shuffle(in_values)
        stdout = io.StringIO()
        with contextlib.redirect_stdout(stdout):
            print_even_values(in_values)
        out_values = stdout.getvalue().split(sep=' ')
        out_values.pop()
        for value in out_values:
            self.assertEqual(int(value) % 2, 0)
        self.assertEqual(len(set(out_values)), int(high / 2))


if __name__ == '__main__':
    unittest.main()
