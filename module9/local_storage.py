import pickle
from abc import ABC, abstractmethod

class Storage(ABC):
    @abstractmethod
    def save(self, object):
        pass
    
    @abstractmethod
    def restore(self):
        pass
    
    @abstractmethod
    def set_file_name(self, name):
        pass


class LocalStorage(Storage):
    def __init__(self, file_name: str = 'data.bin') -> None:
        self.__file_name = file_name
        
    def set_file_name(self, name: str):
        self.__file_name = name
        
    def save(self, object):
        with open(self.__file_name, "wb") as fh:
            pickle.dump(object, fh)
            
    def restore(self):
        with open(self.__file_name, "rb") as fh:
            unpacked = pickle.load(fh)
            return unpacked
