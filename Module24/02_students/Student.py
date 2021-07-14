class Student:

    def __init__(self, name_surname, group_number, acd_performance):
        self.name_surname = name_surname
        self.group_number = group_number
        self.acd_performance = acd_performance

    def print_student_info(self):
        print('\nName and Surname:', self.name_surname)
        print('Group number:', self.group_number)
        print('Academic performance:', self.acd_performance)



