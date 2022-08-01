from assistant_command import AssistantCommand
from error_decorator import *
from assistant_exceptions import *
from address_book import AddressBook

CONTACTS = AddressBook()

@input_error
def handle_hello(value) -> str:
    return 'How can I help you?'

@input_error   
def handle_add(contact: list[str]) -> str:
    if len(contact) != 2:
        raise UnknownAssistentValue('Give me name and phone please.')
    CONTACTS[contact[0].lower()] = contact[1]
    return 'Contact added successfully!'

@input_error
def handle_change(contact: list[str]) -> str:
    if len(contact) != 2:
        raise UnknownAssistentValue('Give me name and phone please.')
    message = 'Contact updated successfully!'
    if contact[0].lower() not in CONTACTS.keys():
        message = 'This contact does not exist for updating.\nSo a new contact was created!'
    handle_add(contact)
    return message

@input_error
def handle_phone(contact: list[str]) -> str:
    if len(contact) != 1:
        raise UnknownAssistentValue('Give me name.')
    return CONTACTS.get(contact[0].lower(), "The specified contact does not exist.")

@input_error
def handle_show(value):
    message = ""
    for i, (k, v) in enumerate(CONTACTS.items()):
        message += f'{i + 1}. {k} {v}\n'
    
    message.strip('\n')
    if not message:
        message = 'Contact list is empty!\n'
    message = "----------------------\n" + message + "----------------------"
    
    return message

@input_error
def handle_exit(value) -> str:
    return 'Good bye!'

@input_error
def handle_help(value) -> str:
    commands = ['HELLO', 'ADD <name> <phone>',
                'CHANGE <name> <phone>', 'PHONE <name>',
                'SHOW ALL', 'GOOD BYE', 'CLOSE', 'EXIT']
    return '\n'.join(commands)
@input_error
def handle_unknown(value) -> str:
    return 'Incorrect Command!!!'

COMMANDS = {
    AssistantCommand.HELLO: handle_hello,
    AssistantCommand.ADD: handle_add,
    AssistantCommand.CHANGE: handle_change,
    AssistantCommand.PHONE: handle_phone,
    AssistantCommand.SHOW: handle_show,
    AssistantCommand.HELP: handle_help,
    AssistantCommand.EXIT: handle_exit,
    AssistantCommand.UNKNOWN: handle_unknown
}


@input_error
def get_handler(command: AssistantCommand):
    if command is AssistantCommand.UNKNOWN:
        raise UnknownAssistentCommand
    return COMMANDS[command]