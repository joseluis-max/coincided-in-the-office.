""" Calculate office time coincided by scheduled """

class Coincided_Office_Time:
    """ Use Case entitie Scheduled """
    def calculate_coincided_office_time(self, dataEngine, name_file):
        schedule = dataEngine.read(name_file)
        List_Employee = []
        for name in schedule.keys():
            List_Employee.append(name)
        for employee_A in range(len(List_Employee)):
            for employee_B in range(employee_A + 1, len(List_Employee)):
                coincided_times = 0
                for date in schedule[List_Employee[employee_A]]:
                    if date in schedule[List_Employee[employee_B]]:
                        coincided_times += 1
                print(f"{List_Employee[employee_A]}-{List_Employee[employee_B]}", end=": ")
                print(coincided_times)
