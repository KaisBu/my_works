from parents import *


def children(number, parent_age):
    child_list = []
    for i in range(number):
        child_name = input(f'\nEnter child {i+1} name: ')

        while True:
            try:
                child_age = int(input(f'Enter child {i+1} age: '))
                if child_age < 0:
                    raise ValueError
                elif parent_age - child_age > 16:
                    child = Child(child_name, child_age)
                    child_list.append(child)
                    break
                else:
                    print('The age difference between the parent and the child must be at least 16 years old')
            except ValueError:
                print('Child age must be positive')

    return child_list


name = input("Enter parent's name: ")

while True:
    age = int(input("Enter parent's age: "))
    if age < 16:
        print("Parent's age must be more than 16 years old")
    else:
        break

number_of_children = int(input('Enter number of children: '))
children_list = children(number_of_children, age)
first_parent = Parents(name, age, children_list)

first_parent.print_info()
first_parent.feed_the_baby(children_list[1])
first_parent.calm_the_child(children_list[0])
first_parent.print_info()
first_parent.calm_the_child(children_list[0])

