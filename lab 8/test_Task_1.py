import unittest
from Task_1 import is_valid_email
class TestIsValidEmail(unittest.TestCase):
    def test_valid_emails(self):
        self.assertTrue(is_valid_email("user@example.com"))
        self.assertTrue(is_valid_email("john.doe123@domain.co.uk"))
        self.assertTrue(is_valid_email("a_b-c.d@sub.domain.com"))
        self.assertTrue(is_valid_email("abc@xyz.io"))
    def test_missing_at_symbol(self):
        self.assertFalse(is_valid_email("userexample.com"))
        self.assertFalse(is_valid_email("user.example.com"))
    def test_multiple_at_symbols(self):
        self.assertFalse(is_valid_email("user@@example.com"))
        self.assertFalse(is_valid_email("user@ex@ample.com"))
    def test_missing_dot(self):
        self.assertFalse(is_valid_email("user@examplecom"))
        self.assertFalse(is_valid_email("user@domain"))
    def test_starts_or_ends_with_at_or_dot(self):
        self.assertFalse(is_valid_email("@user@example.com"))
        self.assertFalse(is_valid_email("user@example.com@"))
        self.assertFalse(is_valid_email(".user@example.com"))
        self.assertFalse(is_valid_email("user@example.com."))
    def test_invalid_characters(self):
        self.assertFalse(is_valid_email("user!@example.com"))
        self.assertFalse(is_valid_email("user#name@example.com"))
        self.assertFalse(is_valid_email("user name@example.com"))

    def test_single_character_local_and_domain(self):
        self.assertTrue(is_valid_email("a@b.c"))

if __name__ == "__main__":
    unittest.main()