from assistant_command import AssistantCommand
from assistant_exceptions import UnknownAssistentCommand, UnknownAssistentValue

class AssistantParser:
    def __init__(self, string: str):
        line_parameters = string.split()
        self.quantity_words_in_command = 0
        self.command = self.__get_command(line_parameters)
        self.value = self.__get_value(line_parameters)
    
    def __get_command(self, parameters: list[str]) -> AssistantCommand:        
        for i in range(AssistantCommand.max_command_words):
            raw_command = ' '.join(parameters[:i + 1])
            command = AssistantCommand(raw_command)
            if command is not AssistantCommand.UNKNOWN:
                self.quantity_words_in_command = len(raw_command.split())
                return command
        raise UnknownAssistentCommand

    def __get_value(self, parameters: list[str]):
        value = parameters[self.quantity_words_in_command:]
        match self.command:
            case AssistantCommand.HELLO | AssistantCommand.SHOW | AssistantCommand.EXIT | AssistantCommand.HELP:
                return []
            case AssistantCommand.PHONE:
                if len(value) == 1:
                    return value
                raise UnknownAssistentValue('Wrong input value. You should input the name of the contact.')
            case _:
                if len(value) == 2:
                    return value
                raise UnknownAssistentValue('Wrong input value. You should enter the contact\'s name and phone number separated by a space.')
        raise UnknownAssistentValue()
        
            
        
        