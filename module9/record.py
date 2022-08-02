from typing import Optional
from fields import Phone, Name, Birthday
from datetime import datetime


class Record:
    def __init__(self, name: Name, birthday: Optional[Birthday], *phones: Phone) -> None:
        self.name = name
        self.birthday = birthday
        self.phones = list(phones)
        
    def add_phone(self, phone: Phone):
        self.phones.insert(0, phone)
        
    def remove_phone(self, phone: Phone):
        self.phones.remove(phone)
        
    def update_phone(self, phone: Phone):
        pass
    
    def days_to_birthday(self) -> Optional[int]:
        if self.birthday:
            birthday_date = self.birthday.datetime
            now = datetime.now()
            delta1 = datetime(now.year, birthday_date.month, birthday_date.day)
            delta2 = datetime(now.year+1, birthday_date.month, birthday_date.day)
            return ((delta1 if delta1 > now else delta2) - now).days
        return None
    
    def __str__(self) -> str:
        phone_list = 'Absent'
        if self.phones:
            phone_list = ', '.join(map(str, self.phones))
        return '%s, %s, %s' % (self.name, phone_list, self.birthday or '')
    
    
# record = Record(Name('Taras'), Birthday('04/08/1991'), Phone('0664245216'))
# print(record)
# print(record.days_to_birthday())