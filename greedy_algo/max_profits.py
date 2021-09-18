import unittest
def get_max_profits(stock_prices: list): 
    if len(stock_prices) < 2:
        raise Exception
    min_price = stock_prices[0]
    profit = 0
    for price in stock_prices:
        # calculate the difference only if we can make a profit
        if min_price < price:
            diff = price - min_price
            # update the profit if to take the max profit
            if diff > profit: 
                profit = diff
        # track minimum cost
        if price < min_price:
            min_price = price
    return profit 


class GreedyAlgoMaxProfitsTestSuite(unittest.TestCase):

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


if __name__=="__main__":
    unittest.main() 


        
        



