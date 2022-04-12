#!/bin/usr/python3
""" Testing file engine """

import unittest
from data_providers.file_engine import FileEngine

class TestFileEngine(unittest.TestCase):
    """ Testing file engine methods """

    def test_read_file(self):
        """ Checking if we can read a file succes"""
        correct_data = {
            "RENE": ["MO10: 00-12: 00", "TU10: 00-12: 00", "TH01: 00-03: 00", "SA14: 00-18: 00", "SU20: 00-21: 00"],
            "ASTRID": ["MO10: 00-12: 00", "TH12: 00-14: 00", "SU20: 00-21: 00"],
            "ANDRES": ["MO10: 00-12: 00", "TH12: 00-14: 00", "SU20: 00-21: 00"]
        }
        fileEngine = FileEngine()
        data = fileEngine.read("data.txt")
        self.assertNotEqual(data, correct_data)

    def test_read_file_doesnt_exit(self):
        """ Checking if we can read a file doesn't exist """
        fileEngine = FileEngine()
        self.assertRaises(FileNotFoundError, fileEngine.read, "where_is_this_file.txt")


if __name__ == '__main__':
    unittest.main()
