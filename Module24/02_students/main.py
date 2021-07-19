from Student import Student


def sort_by_mean(some_student):
    mean_num = sum(some_student.acd_performance) / len(some_student.acd_performance)
    return mean_num


students_num = int(input('Enter number of student: '))

student_list_1 = [
    Student(
        input('\nEnter student name and surname: '),
        input('Enter group number: '),
        [int(input(f'Enter academic performance {i + 1}: ')) for i in range(5)]
    )
    for _ in range(students_num)
]

student_list_1.sort(key=sort_by_mean)

for i_student in student_list_1:
    i_student.print_student_info()
