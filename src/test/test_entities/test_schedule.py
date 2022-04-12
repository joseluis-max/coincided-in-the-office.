""" Unit test for Schedule class """
from entities.Schedule import Schedule
import unittest


class test_schedule(unittest.TestCase):
    
    def test_singleton_pattern(self):
        data = {
            "RENE": ["MO10: 00-12: 00", "TU10: 00-12: 00", "TH01: 00-03: 00", "SA14: 00-18: 00", "SU20: 00 - 21: 00"],
            "ASTRID": ["MO10: 00-12: 00", "TH12: 00-14: 00", "SU20: 00-21: 00"],
            "ANDRES": ["MO10: 00-12: 00", "TH12: 00-14: 00", "SU20: 00-21: 00"]
        }
        data1 = Schedule()