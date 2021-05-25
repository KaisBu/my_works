a = [1, 5, 3]
b = [1, 5, 1, 5]
c = [1, 3, 1, 5, 3, 3]

a.extend(b)
print('Number of digits 5 at the first merge:', a.count(5))

for num in a:
    if num == 5:
        a.remove(num)

a.extend(c)
print('Number of digits 3 at the second merge:', a.count(3))
print('Final list:', a)
