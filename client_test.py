import unittest
from client3 import getDataPoint
from client3 import getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], (quote['top_bid']['price'] + quote['top_ask']['price'])/2))

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], (quote['top_bid']['price'] + quote['top_ask']['price'])/2))

  """ ------------ Add more unit tests ------------ """

  def test_getRatio_calculateRatios(self):
    # Test Case 1: price_a is greater than price_b
    price_a = 10.0
    price_b = 2.0
    expected_ratio = price_a / price_b
    # Assertion for this test case below
    self.assertEqual(getRatio(price_a, price_b), expected_ratio)

    # Test Case 2: price_b is greater than price_a
    price_a = 2.0
    price_b = 10.0
    expected_ratio = price_a / price_b
    # Assertion for this test case below
    self.assertEqual(getRatio(price_a, price_b), expected_ratio)

    # Test Case 3: price_a and price_b are equal
    price_a = 5.0
    price_b = 5.0
    expected_ratio = price_a / price_b
    # Assertion for this test case below
    self.assertEqual(getRatio(price_a, price_b), expected_ratio)

    # Test Case 4: price_b is 0
    price_a = 10.0
    price_b = 0.0
    # Assertion for this test case below
    self.assertIsNone(getRatio(price_a, price_b))

    # Test Case 5: price_a is 0
    price_a = 0.0
    price_b = 10.0
    expected_ratio = 0.0    # Define the expected ratio when price_a is 0; 0 / n will always be 0
    # Assertion for this test case below
    self.assertEqual(getRatio(price_a, price_b), expected_ratio)




if __name__ == '__main__':
    unittest.main()
