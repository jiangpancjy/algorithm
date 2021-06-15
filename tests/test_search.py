import unittest

from searches.binary_search import binary_search


class TestSearch(unittest.TestCase):

    def test_binary_search(self):
        self.assertEqual(binary_search([1, 2, 3, 4, 5, 6], 4), 3)
        self.assertEqual(binary_search([1, 2, 3, 4, 5, 6], 1), 0)
        self.assertEqual(binary_search([1, 2, 3, 4, 5, 6], 6), 5)
        self.assertEqual(binary_search([1, 2, 3, 4, 5, 6], -1), -1)
        self.assertEqual(binary_search([1, 2, 3, 4, 5, 6], 7), -1)