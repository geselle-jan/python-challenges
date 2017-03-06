import unittest
from leftpad import leftpad


class TestCombineListsFunction(unittest.TestCase):

    def setUp(self):
        self.params = [
            [12345, 8],
            [23456, 5],
            [34567, 3],
            [45678, 0]
        ]

    def test_length_increase(self):
        result = leftpad(*self.params[0])
        self.assertEqual(result, '00012345')

    def test_length_identical(self):
        result = leftpad(*self.params[1])
        self.assertEqual(result, '23456')

    def test_length_decrease(self):
        result = leftpad(*self.params[2])
        self.assertEqual(result, '567')

    def test_length_zero(self):
        result = leftpad(*self.params[3])
        self.assertEqual(result, '')


if __name__ == '__main__':
    unittest.main()