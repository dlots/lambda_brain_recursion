import unittest
import io
import contextlib
from recursive_even_values import recursive_even_values


class TestRecursiveEvenValues(unittest.TestCase):
    def test_recursive_even_values(self):
        stdout = io.StringIO()
        with contextlib.redirect_stdout(stdout):
            recursive_even_values(list(range(50000)))
        values = stdout.getvalue().split(sep=' ')
        values.pop()
        for value in values:
            self.assertEqual(int(value) % 2, 0)


if __name__ == '__main__':
    unittest.main()
