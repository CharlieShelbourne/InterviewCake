import unittest
from greedy_algo.max_profits import get_max_profits

class MaxProfitsTestSuite(unittest.TestCase):

    def test_get_max_profits(self):
       profit = get_max_profits(stock_prices=[10, 7, 5, 8, 11, 9])
       self.assertEqual(profit, 6)

    def min_reset(self):
       profit = get_max_profits(stock_prices=[10, 7, 5, 8, 11, 4, 9])
       self.assertEqual(profit, 6)

    def no_price_change(self):
       profit = get_max_profits(stock_prices=[10, 10, 10])
       self.assertEqual(profit, 0)

    def profit_change(self):
       profit = get_max_profits(stock_prices=[10, 7, 5, 8, 11, 4, 12])
       self.assertEqual(profit, 8)

    def price_goes_down(self):
       profit = get_max_profits(stock_prices=[10, 7, 5, 4])
       self.assertEqual(profit, 0)

    def large_profit_small_profit(self):
       profit = get_max_profits(stock_prices=[10, 4, 12, 2, 8])
       self.assertEqual(profit, 8)

    def test_error_with_empty_prices(self):
        with self.assertRaises(Exception):
            get_max_profit([])

    def test_error_with_one_price(self):
        with self.assertRaises(Exception):
            get_max_profit([1])


class HighestProdOfThreeTestSuit(unittest.TestCase):

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


if __name__=="__main__":
    unittest.main()