import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = SimpleCalculator()

    def test_addition(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)

    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(10, 5), 5)
        self.assertEqual(self.calc.subtract(5, 10), -5)

    def test_multiplication(self):  # expected by checker
        self.assertEqual(self.calc.multiply(3, 4), 12)
        self.assertEqual(self.calc.multiply(-2, 2), -4)

    def test_division(self):  # rename from test_divide
        self.assertEqual(self.calc.divide(10, 2), 5.0)
        self.assertEqual(self.calc.divide(7, 2), 3.5)
        self.assertEqual(self.calc.divide(9, 3), 3.0)
        self.assertEqual(self.calc.divide(5, 0), None)

if __name__ == '__main__':
    unittest.main()
