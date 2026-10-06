import unittest
from calc.calc import Calculator

class CalculatorTestCase(unittest.TestCase):
    def setUp(self):
        # Setup code before each test method
        self.calculator = Calculator()

    def tearDown(self):
        # Cleanup code after each test method
        pass

    def test_add(self):
        result = self.calculator.add(2, 3)
        self.assertEqual(result, 5)

    def test_sub(self):
        result = self.calculator.sub(5, 3)
        self.assertEqual(result, 2, msg="Deu ruim")

    def test_mut(self):
        result = self.calculator.mut(4, 3)
        self.assertEqual(result, 12)

    def test_div(self):
        result = self.calculator.div(10, 2)
        self.assertEqual(result, 5)

    def test_divi_by_zero(self):
        with self.assertRaises(ValueError):
            self.calculator.div(10, 0)
