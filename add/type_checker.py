import re
from datetime import datetime

class TypeChecker:
    def __init__(self, value: str):
        self.value = value
        self.type = self._determine_type()
    
    def _determine_type(self):
        if self._is_email():
            return "email"
        if self._is_phone():
            return "phone"
        if self._is_date():
            return "date"
        return "text"
    
    def _is_email(self):
        return bool(re.fullmatch(r'^[\w-]+@[\w\.-]+\.\w+$', self.value))
    
    def _is_phone(self):
        return bool(re.fullmatch(r'^\+7 \d{3} \d{3} \d{2} \d{2}$', self.value))
    
    def _is_date(self):
        try:
            parts = self.value.replace('-', '.').split('.')
            if len(parts) == 3:
                day, month, year = map(int, parts)
                datetime(year=year, month=month, day=day)
                return True
        except:
            return False
        return False