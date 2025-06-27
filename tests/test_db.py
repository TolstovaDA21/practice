import unittest
from database.db import FormDatabase
import os

class TestDatabase(unittest.TestCase):
    def setUp(self):
        self.test_db_path = 'tests/test_data/test_forms.json'
        self.db = FormDatabase(self.test_db_path)
        
    def tearDown(self):
        if os.path.exists(self.test_db_path):
            os.remove(self.test_db_path)
    
    def test_add_and_find_form(self):
        form = {"name": "Contact", "email": "email", "phone": "phone"}
        doc_id = self.db.add_form(form)
        results = self.db.find_forms({"email": "email"})
        self.assertEqual(len(results), 1)