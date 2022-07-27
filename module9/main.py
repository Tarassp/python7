from email import message
from assistant_parser import AssistantParser
from assistant_command import AssistantCommand
from assistant import Assistant

def main():
    assistant = Assistant()
    message = ''
    while True:
        line = input("Enter your command(type 'help' for more info): ")
        try:
            parser = AssistantParser(line)
            match parser.command:
                case AssistantCommand.HELLO:
                    message = assistant.say_hello()
                case AssistantCommand.ADD:
                    message = assistant.add_contact(parser.value)
                case AssistantCommand.CHANGE:
                    message = assistant.change_contact(parser.value)
                case AssistantCommand.PHONE:
                    contact_name = parser.value[0]
                    message = assistant.get_phone(contact_name)
                case AssistantCommand.SHOW:
                    message = assistant.get_contacts()
                case AssistantCommand.HELP:
                    message = assistant.get_command_descripions()
                case AssistantCommand.EXIT:
                    message = assistant.say_exit()
            
            print(message)
            
            if parser.command is AssistantCommand.EXIT:
                break
            
        except Exception as e:
            print(e)
    
main()