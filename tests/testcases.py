import unittest


class TestCase(unittest.TestCase):

    def assertRaisesRegexpForIndexType(self, *args, **kwargs):
        self.assertRaisesRegex(
            TypeError,
            'linked list index must be an integer',
            *args,
            **kwargs,
        )

    def assertRaisesRegexpForIndexRange(self, *args, **kwargs):
        self.assertRaisesRegex(
            IndexError,
            'linked list index out of range',
            *args,
            **kwargs,
        )


