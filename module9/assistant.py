class Assistant:
    
    def __init__(self) -> None:
        self.contacts = dict[str,str]()
        
    def add_contact(self, contact: list[str]) -> str:
        self.contacts[contact[0].lower()] = contact[1]
        return 'Contact added successfully!'
    
    def change_contact(self, contact: list[str]) -> str:
        message = 'Contact updated successfully!'
        if contact[0].lower() not in self.contacts.keys():
            message = 'This contact does not exist for updating.\nSo a new contact was created!'
        self.add_contact(contact)
        return message
    
    def say_hello(self) -> str:
        return 'How can I help you?'
    
    def get_phone(self, contact_name: str) -> str:
        return self.contacts.get(contact_name.lower(), "The specified contact does not exist.")
    
    def get_contacts(self):
        message = ""
        for i, (k, v) in enumerate(self.contacts.items()):
            message += f'{i + 1}. {k} {v}\n'
        
        message.strip('\n')
        message = "----------------------\n" + message + "----------------------"
        
        return message or 'Contact list is empty!'

    def say_exit(self) -> str:
        return 'Good bye!'
    
    def get_command_descripions(self) -> str:
        commands = ['HELLO', 'ADD <name> <phone>',
                    'CHANGE <name> <phone>', 'PHONE <name>',
                    'SHOW ALL', 'GOOD BYE', 'CLOSE', 'EXIT']
        return '\n'.join(commands)