import unittest
from app import is_valid_email, rectangle_area, filter_even_numbers, convert_date_format, is_palindrome

class TestEmailValidation(unittest.TestCase):
    def test_valid_email(self):
        self.assertTrue(is_valid_email("example@example.com"))

    def test_missing_at_symbol(self):
        self.assertFalse(is_valid_email("example.com"))

    def test_no_domain(self):
        self.assertFalse(is_valid_email("user@"))

    def test_empty_string(self):
        self.assertFalse(is_valid_email(""))

    def test_invalid_characters(self):
        self.assertFalse(is_valid_email("user!@example.com"))

class TestRectangleArea(unittest.TestCase):
    def test_valid_area(self):
        self.assertEqual(rectangle_area(5, 10), 50)

    def test_zero_area(self):
        self.assertEqual(rectangle_area(0, 10), 0)

    def test_negative_width(self):
        self.assertIsNone(rectangle_area(-5, 10))

    def test_negative_height(self):
        self.assertIsNone(rectangle_area(5, -10))

    def test_both_zero(self):
        self.assertEqual(rectangle_area(0, 0), 0)
   
    def test_valid_area(self):
        self.assertEqual(rectangle_area(5, 10), 50)  # Typowy przypadek

    def test_not_equal_area(self):
        self.assertNotEqual(rectangle_area(5, 10), 0)  # Wynik nie może być równy 0


class TestFilterEvenNumbers(unittest.TestCase):
    def test_all_even_numbers(self):
        self.assertEqual(filter_even_numbers([2, 4, 6]), [2, 4, 6])

    def test_mixed_numbers(self):
        self.assertEqual(filter_even_numbers([1, 2, 3, 4]), [2, 4])

    def test_no_even_numbers(self):
        self.assertEqual(filter_even_numbers([1, 3, 5]), [])

    def test_empty_list(self):
        self.assertEqual(filter_even_numbers([]), [])

    def test_large_numbers(self):
        self.assertEqual(filter_even_numbers([1000, 999, 998]), [1000, 998])

class TestConvertDateFormat(unittest.TestCase):
    def test_valid_date(self):
        self.assertEqual(convert_date_format("01-12-2023"), "2023-12-01")

    def test_invalid_date_format(self):
        with self.assertRaises(ValueError):
            convert_date_format("20231201")

    def test_empty_date(self):
        with self.assertRaises(ValueError):
            convert_date_format("")

    def test_incorrect_separator(self):
        with self.assertRaises(ValueError):
            convert_date_format("01.12.2023")
    

class TestIsPalindrome(unittest.TestCase):
    def test_valid_palindrome(self):
        self.assertTrue(is_palindrome("racecar"))

    def test_mixed_case_palindrome(self):
        self.assertTrue(is_palindrome("RaceCar"))

    def test_non_palindrome(self):
        self.assertFalse(is_palindrome("hello"))

    def test_palindrome_with_spaces(self):
        self.assertTrue(is_palindrome("A man a plan a canal Panama"))

    def test_empty_string(self):
        self.assertTrue(is_palindrome(""))

if __name__ == "__main__":
    unittest.main()
