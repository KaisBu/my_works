from company import *


def input_info(specialty):
    for i in range(3):
        name = input('\nEnter name of {} {}: '.format(specialty, i + 1))
        surname = input('Enter surname of {} {}: '.format(specialty, i + 1))

        while True:
            try:
                age = int(input("Enter {}'s age: ".format(specialty)))
                if 0 <= age <= 100:
                    raise ValueError
                break
            except ValueError:
                print('Age should be integer and positive')

        if specialty == 'manger':
            employee_list.append(Manager(name, surname, age))

        elif specialty == 'agent':
            while True:
                try:
                    volume_of_sales = int(input('Enter volume of sales: '))
                    break
                except ValueError:
                    print('Volume of sales be integer')
            employee_list.append(Agent(name, surname, age, volume_of_sales))

        elif specialty == 'worker':
            while True:
                try:
                    hours = int(input('Enter the number of hours worked: '))
                    break
                except ValueError:
                    print('The number of hours worked should be integer')
            employee_list.append(Worker(name, surname, age, hours))


def sum_salary():
    summ = 0

    for i_employee in employee_list:
        summ += i_employee.get_salary()

    return summ


employee_list = []
input_info('manger')
input_info('agent')
input_info('worker')
print('\nAmount of wages:', sum_salary())





