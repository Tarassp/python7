from clean_folder.folder_cleaner import FolderCleaner
from clean_folder.logger import FileLogger
from clean_folder.normalizer import NameNormalizer
import sys

def main():
    try:
        folder_to_clean = sys.argv[1]
    except:
        raise Exception("Provide the correct path to the folder.")
    cleaner = FolderCleaner(folder_to_clean, NameNormalizer(), FileLogger())
    cleaner.clean()
