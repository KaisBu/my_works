import math


class Square:
    """
    Базовый класс Квадрат

    args and attrs:
        length: int - ширина стороны
    """

    def __init__(self, length: int) -> None:
        self._length = length

    @property
    def length(self) -> int:
        return self._length

    @length.setter
    def length(self, length: int) -> None:
        self._length = length

    def square(self) -> int:
        return self._length ** 2

    def perimeter(self) -> int:
        return 4 * self._length


class Triangle:
    """
    Базовый класс Треугольник

    args and attrs:
        base: int - основание
        height: int - высота
    """

    def __init__(self, base: int, height: int) -> None:
        self._base = base
        self._height = height

    @property
    def base(self) -> int:
        return self._base

    @base.setter
    def base(self, base) -> None:
        self._base = base

    @property
    def height(self) -> int:
        return self._height

    @height.setter
    def height(self, height) -> None:
        self._height = height

    def square(self) -> float:
        return 1 / 2 * self._base * self._height

    def perimeter(self) -> float:
        hypotenuse = math.sqrt((1 / 2 * self._base) ** 2 + self._height ** 2)
        return 2 * hypotenuse + self._base


class Cube(Square):
    """
    Класс Куб: родительский класс Square
    """

    def __init__(self, length: int) -> None:
        super().__init__(length)
        self.surface = [Square(length) for _ in range(6)]

    def surface_area(self) -> int:
        return 6 * self.length ** 2


class Pyramid(Triangle):
    """
    Класс Пирамида: родительский класс Triangle
    """
    def __init__(self, base: int, height: int) -> None:
        super().__init__(base, height)
        self.surface = [Square(base) if i == 0 else Triangle(base, height)
                        for i in range(5)]

    def surface_area(self) -> float:
        sum_squares = 0
        for fig in self.surface:
            sum_squares += fig.square()
        return sum_squares


cube1 = Cube(5)
print(cube1.surface_area())

pyr1 = Pyramid(2, 2)
print(pyr1.surface_area())





