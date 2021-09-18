import unittest
from greedy_algo.max_profits import get_max_profits

class GreedyAlgoTestSuite(unittest.TestCase):

    def test_get_max_profits(self):
       profit = get_max_profits(stock_prices=[10, 7, 5, 8, 11, 9])
       self.assertEqual(profit, 6) 

if __name__=="__main__":
    unittest.main()