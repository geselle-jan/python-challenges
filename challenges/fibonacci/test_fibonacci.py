import unittest
from fibonacci import fib


class TestFibonacciFunction(unittest.TestCase):

    def setUp(self):
        self.params = [
            [0,  0],
            [1,  1],
            [2,  1],
            [3,  2],
            [4,  3],
            [5,  5],
            [6,  8],
            [7, 13],
            [8, 21]
        ]

    def test_n1(self):
        n = 1
        self.assertEqual(fib(self.params[n - 1][0]), self.params[n - 1][1])

    def test_n2(self):
        n = 2
        self.assertEqual(fib(self.params[n - 1][0]), self.params[n - 1][1])

    def test_n3(self):
        n = 3
        self.assertEqual(fib(self.params[n - 1][0]), self.params[n - 1][1])

    def test_n4(self):
        n = 4
        self.assertEqual(fib(self.params[n - 1][0]), self.params[n - 1][1])

    def test_n5(self):
        n = 5
        self.assertEqual(fib(self.params[n - 1][0]), self.params[n - 1][1])

    def test_n6(self):
        n = 6
        self.assertEqual(fib(self.params[n - 1][0]), self.params[n - 1][1])

    def test_n7(self):
        n = 7
        self.assertEqual(fib(self.params[n - 1][0]), self.params[n - 1][1])

    def test_n8(self):
        n = 8
        self.assertEqual(fib(self.params[n - 1][0]), self.params[n - 1][1])

    def test_n9(self):
        n = 9
        self.assertEqual(fib(self.params[n - 1][0]), self.params[n - 1][1])


if __name__ == '__main__':
    unittest.main()