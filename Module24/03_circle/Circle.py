import math


class Circle:

    def __init__(self, radius=1, x=0, y=0):
        self.x = x
        self.y = y
        self.radius = radius

    def circle_area(self):
        return math.pi * self.radius ** 2

    def circle_perimeter(self):
        return 2 * math.pi * self.radius

    def increase_circle(self, number):
        self.radius = self.radius * number

    def intersection_circles(self, some_circle):

        if math.sqrt((self.x - some_circle.x) ** 2 +
                     (self.y - some_circle.y) ** 2) > (self.radius + some_circle.radius):
            print('The circles do not intersect')
        else:
            print('The circles intersect')

    def print_info(self):
        print('Center point {}:{}\nRadius: {}\n'.format(
            self.x, self.y, self.radius
        ))

