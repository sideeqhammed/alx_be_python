import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
  def setUp(self):
    """Set up the SimpleCalculator instance before each test."""
    self.calc = SimpleCalculator()

  def test_addition(self):
    """Test the addition method"""

    # self.assertEqual(SimpleCalculator().add(3,2), 5)
    self.assertEqual(self.calc.add(3, 2), 5)
    self.assertEqual(self.calc.add(-2, 3), 1)
    self.assertEqual(self.calc.add(-3, -2), -5)

  def test_subtraction(self):
    """Test the subtract method"""

    # self.assertEqual(SimpleCalculator().subtract(3,2), 5)
    self.assertEqual(self.calc.subtract(3, 2), 1)
    self.assertEqual(self.calc.subtract(-2, 3), -5)
    self.assertEqual(self.calc.subtract(-3, -2), -1)

  def test_multiplication(self):
    """Test the multiply method"""

    # self.assertEqual(SimpleCalculator().multiply(3,2), 5)
    self.assertEqual(self.calc.multiply(3, 2), 6)
    self.assertEqual(self.calc.multiply(-2, 3), -6)
    self.assertEqual(self.calc.multiply(-3, -2), 6)

  def test_division(self):
    """Test the divide method"""

    # self.assertEqual(SimpleCalculator().divide(3,2), 5)
    self.assertEqual(self.calc.divide(4, 2), 2)
    self.assertEqual(self.calc.divide(-4, 2), -2.0)
    self.assertEqual(self.calc.divide(-4, -2), 2.0)
    self.assertEqual(self.calc.divide(4, 0), None)

if __name__ == "__main__":
  unittest.main()