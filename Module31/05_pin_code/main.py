import itertools


for item in itertools.combinations([i for i in range(10)], 4):
    print(''.join((str(i) for i in item)))


