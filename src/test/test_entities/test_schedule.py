""" Unit test for Schedule class """
import unittest
from src.entities.Schedule import Schedule


class testSchedule(unittest.TestCase):
    """ Testing Schedule Class """
    
    def test_instance(self):
        """ Testing if the instance have the correct data """
        data_A = {
            "RENE": ["MO10: 00-12: 00", "TU10: 00-12: 00", "TH01: 00-03: 00", "SA14: 00-18: 00", "SU20: 00 - 21: 00"],
            "ASTRID": ["MO10: 00-12: 00", "TH12: 00-14: 00", "SU20: 00-21: 00"],
            "ANDRES": ["MO10: 00-12: 00", "TH12: 00-14: 00", "SU20: 00-21: 00"]
        }
        data_B = Schedule(data_A).schedule
        self.assertEqual(data_A, data_B)


if __name__ == '__main__':
    unittest.main()