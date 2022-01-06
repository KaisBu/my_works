import math
import time


def prime_nums(max_num: int):
    for num in range(1, max_num + 1):
        is_prime = True
        for i in range(2, int(math.sqrt(max_num)) + 1):
            if num <= i:
                break
            elif num % i == 0:
                is_prime = False
                break
        if is_prime:
            yield num
    return


start_time = time.time()
print(list(filter(lambda x: all(map(lambda y: x % y != 0, range(2, x))), range(1, 1001))))
print('Working time with one string code:', round(time.time() - start_time, 5), end='\n\n')

numbers = []
start_time = time.time()
for number in prime_nums(1000):
    numbers.append(number)
print(numbers)
print('Working time with generator:', round(time.time() - start_time, 5))
