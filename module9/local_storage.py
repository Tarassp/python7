import pickle
from abc import abstractmethod
from typing import Protocol

class StorageInterface(Protocol):
    @abstractmethod
    def save(self, object, filename):
        raise NotImplementedError
    
    @abstractmethod
    def load(self, filename):
        raise NotImplementedError


class LocalStorage(StorageInterface):
    def __init__(self, filename) -> None:
        self._default_filename = filename
    
    def save(self, object, filename = None):
        with open(filename or self._default_filename, "wb") as fh:
            pickle.dump(object, fh)
            
    def load(self, filename = None):
        with open(filename or self._default_filename, "rb") as fh:
            unpacked = pickle.load(fh)
            return unpacked
