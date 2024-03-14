import unittest

class Calculator:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract(a, b):
        return a - b

    @staticmethod
    def multiply(a, b):
        return a * b

    @staticmethod
    def divide(a, b):
        if b == 0:
            raise ValueError("Division by zero is undefined")
        return a / b

    @staticmethod
    def power(a, b):
        if a == 0 and b == 0:
            raise ArithmeticError("0 raised to the power of 0 is undefined")
        return a ** b

    @staticmethod
    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    @staticmethod
    def lcm(a, b):
        return abs(a * b) // Calculator.gcd(a, b)

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

    def test_multiply(self):
        # Arrange
        a = 4
        b = 6
        expected_product = 24

        # Act
        result = Calculator.multiply(a, b)

        # Assert
        self.assertEqual(result, expected_product, "Multiplication is not calculated correctly")

    def test_divide(self):
        # Arrange
        a = 20
        b = 5
        expected_quotient = 4

        # Act
        result = Calculator.divide(a, b)

        # Assert
        self.assertEqual(result, expected_quotient, "Division is not calculated correctly")

    def test_divide_by_zero(self):
        # Arrange
        a = 20
        b = 0

        # Act & Assert
        with self.assertRaises(ValueError):
            Calculator.divide(a, b)

    def test_power(self):
        # Arrange
        base = 2
        exponent = 3
        expected_result = 8

        # Act
        result = Calculator.power(base, exponent)

        # Assert
        self.assertEqual(result, expected_result, "Power is not calculated correctly")

    def test_power_zero_to_zero_exception(self):
        # Act & Assert
        with self.assertRaises(ArithmeticError):
            Calculator.power(0, 0)

    def test_gcd(self):
        # Arrange
        a = 24
        b = 36
        expected_result = 12

        # Act
        result = Calculator.gcd(a, b)

        # Assert
        self.assertEqual(result, expected_result, "GCD is not calculated correctly")

    def test_lcm(self):
        # Arrange
        a = 12
        b = 18
        expected_result = 36

        # Act
        result = Calculator.lcm(a, b)

        # Assert
        self.assertEqual(result, expected_result, "LCM is not calculated correctly")

if __name__ == '__main__':
    unittest.main()
