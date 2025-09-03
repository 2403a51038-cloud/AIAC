import unittest
from Task_3 import is_sentence_palindrome
class TestIsSentencePalindrome(unittest.TestCase):
    def test_simple_palindromes(self):
        self.assertTrue(is_sentence_palindrome("racecar"))
        self.assertTrue(is_sentence_palindrome("madam"))
    def test_with_spaces_and_punctuation(self):
        self.assertTrue(is_sentence_palindrome("A man, a plan, a canal: Panama"))
        self.assertTrue(is_sentence_palindrome("Was it a car or a cat I saw?"))
        self.assertTrue(is_sentence_palindrome("No 'x' in Nixon"))
    def test_case_insensitivity(self):
        self.assertTrue(is_sentence_palindrome("Never Odd Or Even"))
        self.assertTrue(is_sentence_palindrome("Able was I ere I saw Elba"))
    def test_non_palindromes(self):
        self.assertFalse(is_sentence_palindrome("hello"))
        self.assertFalse(is_sentence_palindrome("OpenAI"))
        self.assertFalse(is_sentence_palindrome("Python programming"))
    def test_empty_and_single_character(self):
        self.assertTrue(is_sentence_palindrome(""))
        self.assertTrue(is_sentence_palindrome("a"))
        self.assertTrue(is_sentence_palindrome("Z"))
    def test_numbers_and_alphanumeric(self):
        self.assertTrue(is_sentence_palindrome("12321"))
        self.assertFalse(is_sentence_palindrome("12345"))
        self.assertTrue(is_sentence_palindrome("1a2b2a1"))

    def test_unicode_letters(self):
        # Accented characters are treated as distinct code points; simple lowercasing is applied
        self.assertTrue(is_sentence_palindrome("été"))  # palindrome with accents
        self.assertFalse(is_sentence_palindrome("réifier"))
if __name__ == "__main__":
    unittest.main()


