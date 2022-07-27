class UnknownAssistentCommand(Exception):
    def __init__(self, message = "You entered the wrong command.\nType 'help' to show possible commands."):
        self.message = message
        super().__init__(self.message)
        
class UnknownAssistentValue(Exception):
    def __init__(self, message = "You entered the wrong value.\nType 'help' to show possible commands."):
        self.message = message
        super().__init__(self.message)