#!/usr/bin/python3
""" Calculating coincided employee time office """
import sys
from src.data_providers.file_engine import FileEngine
from src.uses_cases.coincided_office_time import Coincided_Office_Time

if __name__ == "__main__":
    coincided_Office_Time = Coincided_Office_Time()
    coincided_Office_Time.calculate_coincided_office_time(FileEngine,
                                                          sys.argv[1])
