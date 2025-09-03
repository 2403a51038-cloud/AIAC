import unittest
from Task_0 import add, subtract, multiply, divide

class TestCalculatorFunctions(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)
        self.assertAlmostEqual(add(2.5, 3.1), 5.6)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(0, 0), 0)
        self.assertEqual(subtract(-1, -1), 0)
        self.assertAlmostEqual(subtract(5.5, 2.2), 3.3)

    def test_multiply(self):
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(-1, 1), -1)
        self.assertEqual(multiply(0, 100), 0)
        self.assertAlmostEqual(multiply(2.5, 4), 10.0)

    def test_divide(self):
        self.assertEqual(divide(6, 3), 2)
        self.assertEqual(divide(0, 1), 0)
        self.assertEqual(divide(5, 2), 2.5)
        self.assertEqual(divide(5, 0), "Error: Division by zero")
        self.assertAlmostEqual(divide(7.5, 2.5), 3.0)

if __name__ == "__main__":
    unittest.main()