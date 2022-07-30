class UnknownAssistentCommand(Exception):
    def __init__(self, message = "You entered the wrong command."):
        self.message = message
        super().__init__(self.message)
        
class UnknownAssistentValue(Exception):
    def __init__(self, message = "You entered the wrong value."):
        self.message = message
        super().__init__(self.message)