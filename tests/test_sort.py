import random
import string
import unittest

from sorts.bubble_sort import bubble_sort
from sorts.quick_sort import quick_sort
from sorts.quick_sort2 import quick_sort2
from sorts.selection_sort import selection_sort
from sorts.insert_sort import insert_sort


class TestSort(unittest.TestCase):

    def test_bubble_sort(self):
        self.assertEqual(bubble_sort([0, 5, 2, 3, 2]), [0, 2, 2, 3, 5])
        self.assertEqual(bubble_sort([]), [])
        self.assertEqual(bubble_sort([-2, -8, -5]), [-8, -5, -2])
        self.assertEqual(bubble_sort(['d', 'a', 'b', 'e', 'c']), ['a', 'b', 'c', 'd', 'e'])
        collection = random.sample(range(-50, 50), 100)
        self.assertEqual(bubble_sort(collection), sorted(collection))
        collection = random.choices(string.ascii_letters + string.digits, k=100)
        self.assertEqual(bubble_sort(collection), sorted(collection))

    def test_quick_sort(self):
        self.assertEqual(quick_sort([0, 5, 2, 3, 2]), [0, 2, 2, 3, 5])
        self.assertEqual(quick_sort([]), [])
        self.assertEqual(quick_sort([-2, -8, -5]), [-8, -5, -2])
        self.assertEqual(quick_sort(['d', 'a', 'b', 'e', 'c']), ['a', 'b', 'c', 'd', 'e'])
        collection1 = random.sample(range(-50, 50), 100)
        collection2 = collection1.copy()
        self.assertEqual(quick_sort(collection1), sorted(collection2))
        collection1 = random.choices(string.ascii_letters + string.digits, k=100)
        collection2 = collection1.copy()
        self.assertEqual(quick_sort(collection1), sorted(collection2))

    def test_quick_sort1(self):
        self.assertEqual(quick_sort2([0, 5, 2, 3, 2], 0, 4), [0, 2, 2, 3, 5])
        self.assertEqual(quick_sort2([], 0, 0), [])
        self.assertEqual(quick_sort2([-2, -8, -5], 0, 2), [-8, -5, -2])
        self.assertEqual(quick_sort2(['d', 'a', 'b', 'e', 'c'], 0, 4), ['a', 'b', 'c', 'd', 'e'])
        collection = random.sample(range(-50, 50), 100)
        self.assertEqual(quick_sort2(collection, 0, 99), sorted(collection))
        collection = random.choices(string.ascii_letters + string.digits, k=100)
        self.assertEqual(quick_sort2(collection, 0, 99), sorted(collection))

    def test_selection_sort(self):
        self.assertEqual(selection_sort([0, 5, 2, 3, 2]), [0, 2, 2, 3, 5])
        self.assertEqual(selection_sort([]), [])
        self.assertEqual(selection_sort([-2, -8, -5]), [-8, -5, -2])
        self.assertEqual(selection_sort(['d', 'a', 'b', 'e', 'c']), ['a', 'b', 'c', 'd', 'e'])
        collection = random.sample(range(-50, 50), 100)
        self.assertEqual(selection_sort(collection), sorted(collection))
        collection = random.choices(string.ascii_letters + string.digits, k=100)
        self.assertEqual(selection_sort(collection), sorted(collection))

    def test_insert_sort(self):
        self.assertEqual(insert_sort([0, 5, 2, 4, 2, 8]), [0, 2, 2, 4, 5, 8])
        self.assertEqual(insert_sort([]), [])
        self.assertEqual(insert_sort([-2, -8, -5]), [-8, -5, -2])
        self.assertEqual(insert_sort(['d', 'a', 'b', 'e', 'c']), ['a', 'b', 'c', 'd', 'e'])
        collection = random.sample(range(-50, 50), 100)
        self.assertEqual(insert_sort(collection), sorted(collection))
        collection = random.choices(string.ascii_letters + string.digits, k=100)
        self.assertEqual(insert_sort(collection), sorted(collection))