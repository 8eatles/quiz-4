import os.path

from FileManager import FileManager


class TextManager(FileManager):
    def __init__(self, filepath, mode):
        super().__init__(filepath, mode, "txt")
