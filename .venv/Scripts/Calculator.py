import unittest

class Calculator:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract(a, b):
        return a - b


class TestCalculator(unittest.TestCase):
    def test_add(self):
        # Arrange
        a = 3
        b = 5
        expected_sum = 8

        # Act
        result = Calculator.add(a, b)

        # Assert
        self.assertEqual(result, expected_sum, "Sum is not calculated correctly")

    def test_subtract(self):
        # Arrange
        a = 10
        b = 3
        expected_difference = 7

        # Act
        result = Calculator.subtract(a, b)

        # Assert
        self.assertEqual(result, expected_difference, "Subtraction is not calculated correctly")


if __name__ == '__main__':
    unittest.main()
