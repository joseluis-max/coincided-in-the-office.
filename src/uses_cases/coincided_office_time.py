""" Calculate office time coincided by scheduled """
from src.entities.Schedule import Schedule

class Coincided_Office_Time:
    """ Use Case entitie Scheduled """
    def calculate_coincided_office_time(self, dataEngine, name_file):
        data = dataEngine.read(name_file)
        schedule = Schedule(data).schedule
        list_employee = list(schedule.keys())
        for employee_A in range(len(list_employee)):
            for employee_B in range(employee_A + 1, len(list_employee)):
                coincided_times = 0
                for date in schedule[list_employee[employee_A]]:
                    if date in schedule[list_employee[employee_B]]:
                        coincided_times += 1
                print(f"{list_employee[employee_A]}-{list_employee[employee_B]}", end=": ")
                print(coincided_times)
