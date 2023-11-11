import unittest
from math_quiz import random_integer, random_operation, calculate_result


class TestMathGame(unittest.TestCase):

    def test_random_integer(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = function_A(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_random_operation(self):
        # Test if the generated operation is one of +, -, *
        valid_operations = ['+', '-', '*']
        for _ in range(1000):
            operation = random_operation()
            self.assertIn(operation, valid_operations)
            
    def test_calculate_result(self):
        # Test if the calculated result is correct for various operations
        test_cases = [
            (5, 2, '+', 7),
            (4, 3, '-', 1),
            (8, 2, '*', 16)]

        for num1, num2, operator, expected_answer in test_cases:
            actual_answer = calculate_result(num1, num2, operator)
            self.assertEqual(actual_answer, expected_answer)

if __name__ == "__main__":
    unittest.main()
