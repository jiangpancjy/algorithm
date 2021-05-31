import random
import string
import unittest

from sorts import Sort


class TestSort(unittest.TestCase):
    sort = Sort()

    def test_bubble_sort(self):
        self.assertEqual(self.sort.bubble_sort([0, 5, 2, 3, 2]), [0, 2, 2, 3, 5])
        self.assertEqual(self.sort.bubble_sort([]), [])
        self.assertEqual(self.sort.bubble_sort([-2, -8, -5]), [-8, -5, -2])
        self.assertEqual(self.sort.bubble_sort(['d', 'a', 'b', 'e', 'c']), ['a', 'b', 'c', 'd', 'e'])
        collection = random.sample(range(-50, 50), 100)
        self.assertEqual(self.sort.bubble_sort(collection), sorted(collection))
        collection = random.choices(string.ascii_letters + string.digits, k=100)
        self.assertEqual(self.sort.bubble_sort(collection), sorted(collection))

