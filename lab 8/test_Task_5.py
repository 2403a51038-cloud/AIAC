import unittest

from Task_5 import convert_date_format


class TestConvertDateFormat(unittest.TestCase):
    def test_convert_valid_date(self):
        self.assertEqual(convert_date_format("2023-11-05"), "05-11-2023")

    def test_preserves_leading_zeros(self):
        self.assertEqual(convert_date_format("2001-01-09"), "09-01-2001")

    def test_raises_on_wrong_separator(self):
        with self.assertRaises(ValueError):
            convert_date_format("2023/11/05")

    def test_raises_on_too_few_parts(self):
        with self.assertRaises(ValueError):
            convert_date_format("2023-11")

    def test_raises_on_too_many_parts(self):
        with self.assertRaises(ValueError):
            convert_date_format("2023-11-05-01")


if __name__ == "__main__":
    unittest.main()


