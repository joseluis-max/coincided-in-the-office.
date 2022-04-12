""" Testing uses_case coincided time office """
import unittest

from src.uses_cases.coincided_office_time import CoincidedOfficeTime
from src.data_providers.file_engine import FileEngine


class TestCoincidedOfficeTime(unittest.TestCase):
    """ Testing algorithm use case """
    def test_empty_file(self):
        """ Testing if we pass a empty file """
        coincidedOfficeTime = CoincidedOfficeTime()
        result = coincidedOfficeTime.calculate_coincided_office_time(FileEngine, "data3.txt")
        self.assertEqual(result, None)
    
    def test_single_employee_file(self):
        """ Testing if we pass a empty file """
        coincidedOfficeTime = CoincidedOfficeTime()
        result = coincidedOfficeTime.calculate_coincided_office_time(FileEngine, "data4.txt")
        self.assertEqual(result, None)


if __name__ == '__main__':
    unittest.main()
