import unittest
from functions import *

class TestFunctions(unittest.TestCase):

    # --- 1. Отсортировать массивy ---
    def test_sort_array_normal(self):
        self.assertEqual(sort_array([3,1,2]), [1,2,3])
    def test_sort_array_empty(self):
        self.assertEqual(sort_array([]), [])
    def test_sort_array_single(self):
        self.assertEqual(sort_array([5]), [5])
    def test_sort_array_duplicates(self):
        self.assertEqual(sort_array([2,1,2]), [1,2,2])

    # --- 2. является палиндромом---
    def test_is_palindrome_true(self):
        self.assertTrue(is_palindrome("level"))
    def test_is_palindrome_false(self):
        self.assertFalse(is_palindrome("hello"))
    def test_is_palindrome_empty(self):
        self.assertTrue(is_palindrome(""))
    def test_is_palindrome_case(self):
        self.assertTrue(is_palindrome("Level"))

    # --- 3. Факториал ---
    def test_factorial_normal(self):
        self.assertEqual(factorial(5), 120)
    def test_factorial_zero(self):
        self.assertEqual(factorial(0), 1)
    def test_factorial_one(self):
        self.assertEqual(factorial(1), 1)
    def test_factorial_negative(self):
        with self.assertRaises(ValueError):
            factorial(-1)

    # --- 4. Число Фибоначчи ---
    def test_fibonacci_zero(self):
        self.assertEqual(fibonacci(0), 0)
    def test_fibonacci_one(self):
        self.assertEqual(fibonacci(1), 1)
    def test_fibonacci_six(self):
        self.assertEqual(fibonacci(6), 8)
    def test_fibonacci_eight(self):
        self.assertEqual(fibonacci(8), 21)

    # --- 5. Найти подстроку ---
    def test_find_substring_present(self):
        self.assertEqual(find_substring("hello world", "world"), 6)
    def test_find_substring_absent(self):
        self.assertEqual(find_substring("hello", "x"), -1)
    def test_find_substring_start(self):
        self.assertEqual(find_substring("abc", "a"), 0)
    def test_find_substring_middle(self):
        self.assertEqual(find_substring("abc", "b"), 1)

    # --- 6. является простым ---
    def test_is_prime_prime(self):
        self.assertTrue(is_prime(7))
    def test_is_prime_nonprime(self):
        self.assertFalse(is_prime(9))
    def test_is_prime_one(self):
        self.assertFalse(is_prime(1))
    def test_is_prime_two(self):
        self.assertTrue(is_prime(2))

    # --- 7. Перевернуть число ---
    def test_reverse_number_positive(self):
        self.assertEqual(reverse_number(123), 321)
    def test_reverse_number_negative(self):
        self.assertEqual(reverse_number(-120), -21)
    def test_reverse_number_overflow(self):
        self.assertEqual(reverse_number(1534236469), 0)
    def test_reverse_number_single(self):
        self.assertEqual(reverse_number(1), 1)

    # --- 8. Преобразовать в римские цифры ---
    def test_to_roman_nine(self):
        self.assertEqual(to_roman(9), "IX")
    def test_to_roman_2025(self):
        self.assertEqual(to_roman(2025), "MMXXV")
    def test_to_roman_one(self):
        self.assertEqual(to_roman(1), "I")
    def test_to_roman_forty_two(self):
        self.assertEqual(to_roman(42), "XLII")

if __name__ == '__main__': 
    unittest.main(verbosity=2)
