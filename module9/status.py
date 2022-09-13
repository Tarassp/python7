from notes_command import NotesCommand

class Status:
    class Request:
        def __init__(self, message: str, command: NotesCommand) -> None:
            self.message = message
            self.command = command

    def __init__(self, response: str | None = None, request: Request | None = None) -> None:
        self.response = response
        self.request = request