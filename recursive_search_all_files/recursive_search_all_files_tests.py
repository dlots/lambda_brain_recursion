import unittest
from recursive_search_all_files import search_all_files


class TestRecursiveSearchAllFiles(unittest.TestCase):
    def test_recursive_search_all_files(self):
        path = 'E:\\test_recursive_search_all_files'
        expected = [
            'E:\\test_recursive_search_all_files\\doc1.txt',
            'E:\\test_recursive_search_all_files\\doc2.txt',
            'E:\\test_recursive_search_all_files\\folder1\\folder2\\doc3.txt',
            'E:\\test_recursive_search_all_files\\folder1\\folder3\\folder5\\doc4.txt'
        ]
        result = search_all_files(path)
        self.assertEqual(len(result), len(expected))
        for file in result:
            self.assertTrue(file in expected)


if __name__ == '__main__':
    unittest.main()
