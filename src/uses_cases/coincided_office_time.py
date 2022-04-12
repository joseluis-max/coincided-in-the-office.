""" Calculate office time coincided by scheduled """

class Coincided_Office_Time:
    """ Use Case entitie Scheduled """
    def calculate_coincided_office_time(self, dataEngine, name_file):
        data = dataEngine.read(name_file)
        List_Employee = []
        for name, time in data.items():
            List_Employee.append(name)
        for employee_A in range(len(List_Employee)):
            for employee_B in range(employee_A + 1, len(List_Employee)):
                hour = 0
                for t in data[List_Employee[employee_A]]:
                    if t in data[List_Employee[employee_B]]:
                        hour += 1
                print(List_Employee[employee_A], List_Employee[employee_B], end=": ->")
                print(hour)
