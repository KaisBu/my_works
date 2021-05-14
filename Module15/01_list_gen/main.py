number = int(input('Enter the number: '))
num_list = []

for num in range(1, abs(number) + 1):
    if num % 2 != 0:
        num_list.append(num)

if number < 0:
    for i in range(len(num_list)):
        num_list[i] *= -1

print('Generated list:\n', num_list)
