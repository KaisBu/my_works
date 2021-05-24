def list_create(num, size):
    lst = []
    for i in range(num):
        element = int(input(f'Enter {size} number {i + 1}: '))
        lst.append(element)
    return lst


number_rollers = int(input('Enter total number of rollers skates: '))
roller_size_list = list_create(number_rollers, 'size of the pare')

number_people = int(input('\nEnter number of peoples: '))
people_size_list = list_create(number_people, 'human foot size')
count = 0

for foot_size in people_size_list:
    for roller_size in roller_size_list:
        if roller_size >= foot_size:
            count += 1
            roller_size_list.remove(roller_size)
            break

print('\nThe largest number of people who can take roller skates', count)
