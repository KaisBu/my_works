import math


class Auto:

    def __init__(self, x, y, angel):
        self.__x = x
        self.__y = y
        self.__angel = angel * math.pi / 180

    def move(self, distance):
        self.set_x(distance)
        self.set_y(distance)

    def set_angel(self, angel):
        self.__angel = angel * math.pi / 180

    def set_x(self, distance):
        self.__x += distance * math.cos(self.__angel)

    def set_y(self, distance):
        self.__y += distance * math.sin(self.__angel)

    def __str__(self):
        return '\nx: {}, Y: {}, angel: {}'.format(
            round(self.__x, 2), round(self.__y, 2),
            round(self.__angel * 180 / math.pi, 2)
        )


class Bus(Auto):

    def __init__(self, x, y, angel):
        super().__init__(x, y, angel)
        self.__passengers_num = 0
        self.__proceeds = 0

    def come_in(self, num):
        self.__passengers_num += num

    def come_out(self, num):
        self.__passengers_num -= num

    def move(self, distance):
        self.set_x(distance)
        self.set_y(distance)
        self.__proceeds += self.__passengers_num * 1.5 * distance

    def __str__(self):
        info = super().__str__()
        return '{}\nNumber of passengers: {}, Proceeds: {}'.format(
            info, self.__passengers_num, round(self.__proceeds, 2)
        )
