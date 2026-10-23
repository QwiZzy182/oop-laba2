import unittest
from regex_checker import EmailValidator

class TestEmailValidator(unittest.TestCase):
    def setUp(self):
        self.validator = EmailValidator()

    def test_valid_email(self):
        result = self.validator.validate_text("Контакты: test.user@mail.ru и admin@company.com")
        self.assertEqual(result, ["test.user@mail.ru", "admin@company.com"])

    def test_invalid_email(self):
        result = self.validator.validate_text("Неверные: @missing.ru, user@.com, user@com")
        self.assertEqual(result, [])

if __name__ == "__main__":
    unittest.main()
