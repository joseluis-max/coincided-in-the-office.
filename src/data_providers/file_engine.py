""" Module for read content of a file"""
from src.interface.controller.filecontroller import InterfaceFileController


class FileEngine(InterfaceFileController):
    """ Reading input from a file """

    @classmethod
    def read(self, file_name):
        """ Reading a file and return it a dictionary """
        file_content = {}
        try:
            with open(file_name, 'r') as file:
                for line in file:
                    split_line = line[:-1].split("=")
                    employee = split_line[0]
                    schedule = split_line[1].split(",")
                    file_content[employee] = schedule
                return file_content
        except FileNotFoundError:
            print("File doesn't exit !")
            raise
