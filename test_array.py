import unittest
# from algorithms import arrays

class TestArray(unittest.TestCase):
    """
    `Test that the result sum of all numbers
    """
    # def test_sum(self):
    #     instance = arrays.Array()
    #     result = instance.sum(6, '1 2 3 4 10 11')
    #     self.assertEqual(result, 31)
    def test_sum(self):
        array_example = [1,9,2,8,3,7,4,6,5]
        result = sum(array_example)
        self.assertEqual(result, 45)

