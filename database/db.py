from tinydb import TinyDB, Query

class FormDatabase:
    def __init__(self, db_path='database/forms.json'):
        self.db = TinyDB(db_path)
    
    def add_form(self, form_data: dict):
        return self.db.insert(form_data)
    
    def find_forms(self, fields: dict):
        Form = Query()
        query = None
        for field, type_ in fields.items():
            if query is None:
                query = (Form[field].exists()) & (Form[field].matches(type_))
            else:
                query &= (Form[field].exists()) & (Form[field].matches(type_))
        return self.db.search(query) 