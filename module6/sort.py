from folder_cleaner import FolderCleaner
from logger import ConsoleLogger, FileLogger
from normalizer import *
import sys

folder_to_clean = sys.argv[1]
cleaner = FolderCleaner(folder_to_clean, NameNormalizer(), FileLogger())
cleaner.clean()
    
