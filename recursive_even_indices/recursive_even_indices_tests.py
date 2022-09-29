import unittest
import io
import contextlib
from recursive_even_indices import print_even_indices


class TestRecursiveEvenIndices(unittest.TestCase):
    def test_recursive_even_indices(self):
        stdout = io.StringIO()
        with contextlib.redirect_stdout(stdout):
            print_even_indices(['even' if i % 2 == 0 else 'odd' for i in range(900)])
        values = stdout.getvalue().split(sep=' ')
        values.pop()
        self.assertEqual(len(values), 450)
        for value in values:
            self.assertEqual(value, 'even')


if __name__ == '__main__':
    unittest.main()
