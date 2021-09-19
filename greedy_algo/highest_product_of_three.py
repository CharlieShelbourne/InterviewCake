import unittest

def highest_product_of_three(ints: list):
    if len(ints) < 3:
        raise Exception
    
    max1 = 0
    max2 = 0
    max3 = 0

    min1 = 0
    min2 = 0
    for int in ints:
        # track 3 largest numbers
        if int > max1:
            max3= max2
            max2 = max1
            max1 = int
        # track most negatvie numbers 
        if int < 0:
            if int < min1:
                min2 = min1
                min1 = int
    
    if min1 < 0 and min2 < 0:
        if min1 * min2 * max1 > max1 * max2 * max3:
            return min1 * min2 * max1

    return max1 * max2 * max3


class GreedyAlgoHighesProdOfThreeTestSuit(unittest.TestCase):

    def test_three_positive_numbers(self):
        result = highest_product_of_three([1, 2, 3])
        self.assertEqual(result, 6)

    def test_long_list_positive_numbers(self):
        result = highest_product_of_three([1, 4, 3, 5, 2, 10, 15, 3])
        self.assertEqual(result, 750)

    def test_three_negative_numbers(self):
        result = highest_product_of_three([-1, 4, 3, 5, 2, -10, -15, 3])
        self.assertEqual(result, 750)

    def test_one_negative_numbers(self):
        result = highest_product_of_three([1, 4, 3, 5, 2, 10, -15, 3])
        self.assertEqual(result, 200)

    def test_less_then_three_numbers(self):
        with self.assertRaises(Exception):
            highest_product_of_three([1, 2])

if __name__=='__main__':
    unittest.main()