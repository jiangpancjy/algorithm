import unittest


class TestCase(unittest.TestCase):

    def assertRaisesRegexpForIndexType(self, *args, **kwargs):
        self.assertRaisesRegex(
            TypeError,
            'Index must be an integer',
            *args,
            **kwargs,
        )

    def assertRaisesRegexpForIndexRange(self, *args, **kwargs):
        self.assertRaisesRegex(
            IndexError,
            'Index out of range',
            *args,
            **kwargs,
        )

    def assertRaisesRegexpForIndexPositive(self, *args, **kwargs):
        self.assertRaisesRegex(
            IndexError,
            'Index must be positive',
            *args,
            **kwargs,
        )


