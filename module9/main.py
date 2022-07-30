from email import message
from assistant_parser import AssistantParser
from assistant_command import AssistantCommand
from assistant import Assistant
from assistant_handlers import get_handler

def main():
    message = ''
    while True:
        line = input("Enter your command: ")
        try:
            parser = AssistantParser(line)
            command = parser.get_command()
            value = parser.get_value()
            message = get_handler(command)(value)
            
            if message:
                print(message)

            if command is AssistantCommand.EXIT:
                break
        except:
            print("Type 'help' to see the commands.")
main()