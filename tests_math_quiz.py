import unittest
from math_quiz import function_a, function_b, function_c


class TestMathQuizFunctions(unittest.TestCase):

    def test_function_a(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = function_a(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_function_b(self):
        # Test if the result is one of the specified operators
        for _ in range(1000):  # Test a large number of random values
            rand_operator = function_b()
            self.assertIn(rand_operator, ['+', '-', '*'])

    def test_function_c(self):
        # Test the calculation of the arithmetic operation for different cases
        test_cases = [
            (5, 2, '+', '5 + 2', 7),
            (8, 3, '-', '8 - 3', 5),
            (4, 6, '*', '4 * 6', 24),
            # Add more test cases as needed
        ]

        for num1, num2, operator, expected_problem, expected_answer in test_cases:
            result = function_c(num1, num2, operator)
            expected_result = (expected_problem, expected_answer)
            self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()
