import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
	def setUp(self):
		self.calc = SimpleCalculator()
	def test_addition(self):
#  self.assertEqual(self.calc.add(2, 3), 5)
		self.assertEqual(self.calc.add(2, 3), 5)
		self.assertEqual(self.calc.add(-1, 1), 0)
		self.assertEqual(self.calc.add(-1, -1), -2)
	def test_subtraction(self):
#  self.assertEqual(self.calc.subtract(5, 2), 3)
		self.assertEqual(self.calc.subtract(5, 2), 3)
		self.assertEqual(self.calc.subtract(-5, -2), -3)
		self.assertEqual(self.calc.subtract(5, -2), 7)
	def test_multiplication(self):
# self.assertEqual(self.calc.multiply(2, 3), 6)
		self.assertEqual(self.calc.multiply(2, 3), 6)
		self.assertEqual(self.calc.multiply(-2, -3), 6)
		self.assertEqual(self.calc.multiply(5, 0), 0)
	def test_division(self):
#  self.assertEqual(self.calc.divide(10, 5), 2.0)
		self.assertEqual(self.calc.divide(10, 5), 2.0)
		self.assertEqual(self.calc.divide(0, 5), 0.0)
		self.assertIsNone(self.calc.divide(10, 0))

