import unittest
from binary_search import binary_search
from merge_sort import merge_sort

class AlgorithmTests(unittest.TestCase):
    def test_binary_search(self):
        self.assertEqual(binary_search([1, 3, 5], 3), 1)
        self.assertEqual(binary_search([1, 3, 5], 4), -1)
        self.assertEqual(binary_search([], 1), -1)
    def test_merge_sort(self):
        self.assertEqual(merge_sort([3, 1, 2, 1]), [1, 1, 2, 3])
        self.assertEqual(merge_sort([]), [])

if __name__ == "__main__": unittest.main()