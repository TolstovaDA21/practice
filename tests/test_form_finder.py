import os
import sys
import unittest
from pathlib import Path

# Добавляем корень проекта в PYTHONPATH
sys.path.insert(0, str(Path(__file__).parent.parent))

from app.form_finder import FormFinder

class TestFormFinder(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.test_db = 'test_db.json'
        # Создаем тестовые данные
        with open(cls.test_db, 'w') as f:
            f.write('[{"form_name": "Test Form", "email": "email"}]')
        
        cls.finder = FormFinder(cls.test_db)
    
    def test_find_matching_forms(self):
        results = self.finder.find_matching_forms({"email": "test@example.com"})
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]['form_name'], "Test Form")
    
    @classmethod
    def tearDownClass(cls):
        if os.path.exists(cls.test_db):
            os.remove(cls.test_db)

if __name__ == '__main__':
    unittest.main()