from unittest.case import TestCase


class MultiParamTestCase(TestCase):
    def test_plus_1(self):
        for expected in range(1, 10):
            with self.subTest(expected):
                self.assertEqual(1, expected)
