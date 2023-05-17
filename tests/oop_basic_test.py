import unittest

from oop_basic import Calculation


class CalculationTestIsPrime(unittest.TestCase):
    def test_with_integer_less_than_two(self):
        test_case_numbers = [-100, 0, 1]
        for n in test_case_numbers:
            self.assertEqual(False, Calculation.is_prime(n))

    def test_with_float_number(self):
        self.assertEqual(False, Calculation.is_prime(2.5))

    def test_with_three(self):
        self.assertEqual(True, Calculation.is_prime(3))

    def test_with_three(self):
        self.assertEqual(True, Calculation.is_prime(5))

    def test_with_even_number(self):
        self.assertEqual(False, Calculation.is_prime(4))
        self.assertEqual(False, Calculation.is_prime(6))


class CalculationTestGenerateListOfPrimeNumbers(unittest.TestCase):
    def test_with_number_less_than_one(self):
        test_case_numbers = [-100, -99, 0]
        for n in test_case_numbers:
            self.assertEqual(len(Calculation.generate_list_of_prime_numbers(n)), 0)

    def test_with_number_equal_one(self):
        list_prime_numbers = Calculation.generate_list_of_prime_numbers(1)
        self.assertEqual(len(list_prime_numbers), 1)
        self.assertEqual(list_prime_numbers[0], 3)

    def test_with_number_equal_five(self):
        list_prime_numbers = Calculation.generate_list_of_prime_numbers(5)
        self.assertEqual(len(list_prime_numbers), 5)
        expected_list_numbers = [3, 5, 7, 11, 13]
        for n in range(0, len(expected_list_numbers)):
            self.assertEqual(expected_list_numbers[n], list_prime_numbers[n])


if __name__ == '__main__':
    unittest.main()
