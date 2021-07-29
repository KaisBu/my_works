from collections.abc import Iterable


class SquareIterator:

    def __init__(self, limit: int) -> None:
        self.count = 0
        self.limit = limit

    def __iter__(self) -> Iterable:
        return self

    def __next__(self) -> int:
        self.count += 1
        if self.count <= self.limit:
            return self.count ** 2
        else:
            raise StopIteration


def my_generator(limit: int) -> Iterable[int]:
    count = 0

    while True:
        count += 1
        if count > limit:
            return
        yield count ** 2


number = int(input('Enter the number: '))
my_iter = SquareIterator(number)
for num in my_iter:
    print(num, end=' ')

print()
for num in my_generator(number):
    print(num, end=' ')

print()
square_gen = (count ** 2 for count in range(1, number + 1))
for num in square_gen:
    print(num, end=' ')
