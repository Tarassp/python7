from ast import Name
from collections import UserDict

from fields import Phone, Name
from record import Record

class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[record.name.value] = record
        
    def find_by_name(self, name: Name) -> Record | None:
        return self.data.get(name.value)
    
    def find_by_phone(self, phone: Phone) -> Record | None:
        for record in self.data.values():
            if phone in record.phones:
                return record