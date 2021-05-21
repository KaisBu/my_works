class_1 = []
class_2 = []

for num in range(160, 177, 2):
    class_1.append(num)

for num in range(162, 181, 3):
    class_2.append(num)

class_1.extend(class_2)
class_1.sort()
print('Sorted list:', class_1)
