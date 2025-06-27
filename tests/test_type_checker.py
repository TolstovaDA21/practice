import unittest
from app.type_checker import TypeChecker

class TestTypeChecker(unittest.TestCase):
    def test_email_detection(self):
        self.assertEqual(TypeChecker("test@example.com").type, "email")
        self.assertEqual(TypeChecker("invalid.email").type, "text")

    def test_phone_detection(self):
        self.assertEqual(TypeChecker("+7 123 456 78 90").type, "phone") 
        self.assertEqual(TypeChecker("81234567890").type, "text")

    def test_date_detection(self):
        test_cases = [
            ("12.05.2023", "date"),
            ("2023-05-12", "date"),
            ("2023/05/12", "text"),  # невалидный формат
            ("not-a-date", "text")
        ]
        for value, expected in test_cases:
            with self.subTest(value=value):
                self.assertEqual(TypeChecker(value).type, expected)

if __name__ == '__main__':
    unittest.main()