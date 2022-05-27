import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInt(unittest.TestCase):
    def test_max_end(self):
        my_list = [5, 2, -7, 0, 9]
        self.assertEqual(max_integer(my_list), 9)

    def test_max_beginning(self):
        my_list = [9, 2, -7, 0, 5]
        self.assertEqual(max_integer(my_list), 9)

    def test_max_middle(self):
        my_list = [5, 2, 7, 0, -9]
        self.assertEqual(max_integer(my_list), 7)

    def test_all_negative(self):
        my_list = [-5, -2, -7, -1, -9]
        self.assertEqual(max_integer(my_list), -1)

    def test_one_element(self):
        my_list = [5]
        self.assertEqual(max_integer(my_list), 5)
    
    def test_list_empty(self):
        my_list = []
        self.assertEqual(max_integer(my_list), None)

    def testWord(self):
        my_list = ['what', 'off', 'gumby']
        self.assertEqual(max_integer(my_list), 'what')

    def testFailBasic(self):
        my_list = [1, 4, 'A']
        self.assertRaises(TypeError, max_integer, my_list)

    def testFailDict(self):
        my_list = {'a': 2, 'b': 1, 'c': 3}
        self.assertRaises(KeyError, max_integer, my_list)

    def testPassDict(self):
        my_list = {0: 'a', 1: 'z', 2: 'c'}
        self.assertEqual(max_integer(my_list), 'z')

if __name__ == '__main__':
    unittest.main()