from tinydb import TinyDB, Query
from .type_checker import TypeChecker 

class FormFinder:
    def __init__(self, db_path='database/forms.json'):
        
        self.db = TinyDB(db_path)
        self.query = Query()

    def find_matching_forms(self, input_data: dict) -> list:
        
        
        field_types = {
            field: TypeChecker(value).type 
            for field, value in input_data.items()
        }

        query = None
        for field, type_ in field_types.items():
            field_query = (self.query[field].exists()) & (self.query[field] == type_)
            query = field_query if query is None else query & field_query

        return self.db.search(query)

if __name__ == "__main__":
    
    finder = FormFinder()
    test_data = {
        "email": "test@example.com",
        "phone": "+7 123 456 78 90"
    }
    results = finder.find_matching_forms(test_data)
    print("Найдены совпадения:", results)