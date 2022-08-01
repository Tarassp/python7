from fields import Phone, Name

class Record:
    def __init__(self, name: Name, *phones: Phone) -> None:
        self.name = name
        self.phones = list(phones)
        
    def add_phone(self, phone: Phone):
        self.phones.insert(0, phone)
        
    def remove_phone(self, phone: Phone):
        self.phones.remove(phone)
        
    def update_phone(self, phone: Phone):
        pass
    
    def __str__(self) -> str:
        phone_list = 'Absent'
        if self.phones:
            phone_list = ', '.join(map(str, self.phones))
            
        return 'Name = %s, Phones = %s' % (self.name, phone_list)