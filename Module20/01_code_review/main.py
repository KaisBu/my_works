students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology', 'swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}


def function(student_dict):
    length = 0
    for dictionary in student_dict.values():
        length += len(dictionary['surname'])

    student_interest = [
        interest
        for dictionary in student_dict.values()
        for interest in dictionary['interests']
    ]

    return student_interest, length


if len(students) != 0:
    for id_student, student in students.items():
        print('{id} - {student_age}'.format(
            id=id_student,
            student_age=student['age']
        ))

    interest_list, total_length = function(students)
    print('All students interests: ', interest_list)
    print('Length of all student surnames: ', total_length)
else:
    print('Tne student dictionary is empty')



