import unittest
from combine_lists import combine_lists


class TestCombineListsFunction(unittest.TestCase):

    def setUp(self):
        self.lists = [
            ['a', 'b', 'c', 'd', 'e'],
            ['1', '2', '3', '4', '5'],
            ['1', '2', '3'],
            ['1', '2', '3', '4', '5', '6', '7'],
            []
        ]

    def test_same_length(self):
        combined_list = combine_lists(self.lists[0], self.lists[1])
        self.assertEqual(combined_list, ['a', '1', 'b', '2', 'c', '3', 'd', '4', 'e', '5'])

    def test_second_smaller(self):
        combined_list = combine_lists(self.lists[0], self.lists[2])
        self.assertEqual(combined_list, ['a', '1', 'b', '2', 'c', '3', 'd', 'e'])

    def test_second_larger(self):
        combined_list = combine_lists(self.lists[0], self.lists[3])
        self.assertEqual(combined_list, ['a', '1', 'b', '2', 'c', '3', 'd', '4', 'e', '5', '6', '7'])

    def test_second_empty(self):
        combined_list = combine_lists(self.lists[0], self.lists[4])
        self.assertEqual(combined_list, ['a', 'b', 'c', 'd', 'e'])


if __name__ == '__main__':
    unittest.main()