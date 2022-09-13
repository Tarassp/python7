from note import Note
from notebook import Notebook
from local_storage import StorageInterface
from notes_command import NotesCommand
from status import Status
from error_decorator import *


class NotesServide:
    def __init__(self, storage: StorageInterface, notes: Notebook) -> None:
        self._notebook = notes
        self._searched_notes: list[Note] = []
        self._selected_note: Note | None = None
        self._storage = storage
        self._handlers = {
            NotesCommand.ADD: self._handle_add,
            NotesCommand.TAGS: self._handle_add_tags,
            NotesCommand.SELECTREQUEST: self._handle_select_request,
            NotesCommand.SELECT: self._handle_select_note,
            NotesCommand.SHOW: self._handle_show_all,
            NotesCommand.SEARCH: self._handle_search,
            NotesCommand.SEARCHBYTAG: self._handle_search_by_tag,
            NotesCommand.SEARCHSELECTING: self._handle_search_selecting,
            NotesCommand.SORTBYTAG: self._handle_sort_by_tag,
            NotesCommand.DELETE: self._handle_delete,
            NotesCommand.CHANGE: self._handle_change,
            NotesCommand.EXIT: self._handle_exit,
            NotesCommand.HELP: self._handle_help,
            NotesCommand.UNKNOWN: self._handle_unknown
        }
    
    @input_error
    def _get_handler(self, command: NotesCommand):
        if command is NotesCommand.UNKNOWN:
            raise UnknownAssistentCommand
        return self._handlers[command]
        
    def handle(self, command: NotesCommand, value: list[str]) -> Status:
        handler = self._get_handler(command)
        return handler(value)
    
    @input_error   
    def _handle_add(self, value: list[str]) -> Status:
        if len(value) < 1:
            raise UnknownAssistentValue('Note cannot be empty!')
        self._selected_note = Note(' '.join(value), [])
        self._notebook.add(self._selected_note)
        request = Status.Request('Enter some tag(s) for your note: ', NotesCommand.TAGS)
        return Status('Note is added successfully!', request)
    
    def _handle_add_tags(self, tags: list[str]) -> Status:
        if self._selected_note:
            self._selected_note.add_tags(tags)
        else:
            return Status("You didn't select note yet. Please use SELECT command first.")
        self._selected_note = None
        if not tags:
            return Status('You skipped adding tags')
        if len(tags) > 1:
            return Status('Tags are added successfully!')
        return Status('Tag is added successfully!')
    
    def _handle_select_request(self, value) -> Status:
        request = Status.Request('Enter some text to find notes or just hit "Enter" to show all notes: ', NotesCommand.SEARCHSELECTING)
        return Status(request = request)
    
    def _handle_search_selecting(self, value: list[str]) -> Status:
        search_status = self._handle_search(value)
        if search_status.response.lower() != 'no result':
            search_status.request = Status.Request('Enter the note number: ', NotesCommand.SELECT)
        return search_status
    
    def _handle_select_note(self, value: list[str]) -> Status:
        note_number = int(value[0])
        if (note_number - 1) < len(self._searched_notes):
            self._selected_note = self._searched_notes[note_number - 1]
        elif len(self._notebook) > 0:
            self._selected_note = self._notebook[0]
        else:
            return Status('Cannot select the note because Notebook is empty.')
        return Status('The note is selted. Use <TAGS>, <CHANGE>, or <DELETE> command to work on it')
    
    @input_error
    def _handle_search(self, value: list[str]) -> Status:
        searched_text = ' '.join(value)
        self._searched_notes = self._notebook.search_all(searched_text)
        if self._searched_notes:
            message = ""
            for i, v in enumerate(self._searched_notes):
                message += f'{i + 1}. {v}\n'
            message.strip('\n')
            message = "----------------------\n" + message + "----------------------"
            return Status(message)
        return Status('No Results')
    
    def _handle_search_by_tag(self, value: list[str]) -> Status:
        return Status("Not implemented")
    
    def _handle_sort_by_tag(self, value: list[str]) -> Status:
        return Status("Not implemented")
    
    def _handle_delete(self, value) -> Status:
        if self._selected_note:
            self._notebook.remove(self._selected_note)
            self._selected_note = None
            return Status("Note is deleted successfully!")
        return Status("You didn't select note yet. Please use SELECT command first.")
    
    def _handle_change(self, value: list[str]) -> Status:
        if self._selected_note:
            self._selected_note.append(' '.join(value))
            self._selected_note = None
            return Status("Note is changed successfully!")
        return Status("You didn't select note yet. Please use SELECT command first.")
        
    @input_error
    def _handle_show_all(self, value) -> Status:
        message = ""
        for i, v in enumerate(self._notebook._notes):
            message += f'{i + 1}. {v}\n'
        
        message.strip('\n')
        if not message:
            message = 'Note List is empty!\n'
        message = "----------------------\n" + message + "----------------------"
        
        return Status(message)
    
    @input_error
    def _handle_exit(self, value) -> Status:
        return Status('Good bye!')

    @input_error
    def _handle_help(self, value) -> Status:
        commands = ['ADD <note>', 'TAGS <tag1, tag2 ...>'
                    'SEARCH <text>',
                    'LOAD <filename>', 'SAVE <filename>',
                    'SHOW ALL', 'GOOD BYE', 'CLOSE', 'EXIT']
        return Status('\n'.join(commands))
    
    @input_error
    def _handle_unknown(value) -> Status:
        return Status('Incorrect Command!!!')