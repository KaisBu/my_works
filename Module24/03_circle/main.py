from Circle import Circle


first_circle = Circle()
second_circle = Circle(2, 5, 7)
third_circle = Circle(1, 6, 7)

print('Area of the first circle:', first_circle.circle_area())
print('Perimeter of the second circle:', second_circle.circle_perimeter())

K = int(input('\nEnter the increase: '))
print('Increasing the third circle by {} times:'.format(K))
third_circle.increase_circle(K)
third_circle.print_info()

print('\nDetecting the intersection of the first and second circle: ')
first_circle.intersection_circles(second_circle)

print('\nDetecting the intersection of the second and third circle: ')
second_circle.intersection_circles(third_circle)

