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

    def test_quick_sort(self):
        self.assertEqual(self.sort.quick_sort([0, 5, 2, 3, 2]), [0, 2, 2, 3, 5])
        self.assertEqual(self.sort.quick_sort([]), [])
        self.assertEqual(self.sort.quick_sort([-2, -8, -5]), [-8, -5, -2])
        self.assertEqual(self.sort.quick_sort(['d', 'a', 'b', 'e', 'c']), ['a', 'b', 'c', 'd', 'e'])
        collection1 = random.sample(range(-50, 50), 100)
        collection2 = collection1.copy()
        self.assertEqual(self.sort.quick_sort(collection1), sorted(collection2))
        collection1 = random.choices(string.ascii_letters + string.digits, k=100)
        collection2 = collection1.copy()
        self.assertEqual(self.sort.quick_sort(collection1), sorted(collection2))

    def test_quick_sort1(self):
        self.assertEqual(self.sort.quick_sort1([0, 5, 2, 3, 2], 0, 4), [0, 2, 2, 3, 5])
        self.assertEqual(self.sort.quick_sort1([], 0, 0), [])
        self.assertEqual(self.sort.quick_sort1([-2, -8, -5], 0, 2), [-8, -5, -2])
        self.assertEqual(self.sort.quick_sort1(['d', 'a', 'b', 'e', 'c'], 0, 4), ['a', 'b', 'c', 'd', 'e'])
        collection = random.sample(range(-50, 50), 100)
        self.assertEqual(self.sort.quick_sort1(collection, 0, 99), sorted(collection))
        collection = random.choices(string.ascii_letters + string.digits, k=100)
        self.assertEqual(self.sort.quick_sort1(collection, 0, 99), sorted(collection))

    def test_selection_sort(self):
        self.assertEqual(self.sort.selection_sort([0, 5, 2, 3, 2]), [0, 2, 2, 3, 5])
        self.assertEqual(self.sort.selection_sort([]), [])
        self.assertEqual(self.sort.selection_sort([-2, -8, -5]), [-8, -5, -2])
        self.assertEqual(self.sort.selection_sort(['d', 'a', 'b', 'e', 'c']), ['a', 'b', 'c', 'd', 'e'])
        collection = random.sample(range(-50, 50), 100)
        self.assertEqual(self.sort.selection_sort(collection), sorted(collection))
        collection = random.choices(string.ascii_letters + string.digits, k=100)
        self.assertEqual(self.sort.selection_sort(collection), sorted(collection))