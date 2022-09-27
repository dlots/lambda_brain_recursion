import unittest
import io
import contextlib
from recursive_even_indices import recursive_even_indices


class TestRecursiveEvenValues(unittest.TestCase):
    def test_recursive_even_values(self):
        stdout = io.StringIO()
        with contextlib.redirect_stdout(stdout):
            recursive_even_indices(['even' if i % 2 == 0 else 'odd' for i in range(50000)])
        values = stdout.getvalue().split(sep=' ')
        values.pop()
        for value in values:
            self.assertEqual(value, 'even')


if __name__ == '__main__':
    unittest.main()
