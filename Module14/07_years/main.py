def digit_count(numb):
    count = 0
    for symbol in str(numb):
        count += 1
    return count


first_year = int(input('Enter first year: '))
second_year = int(input('Enter second year: '))

count1 = digit_count(first_year)
count2 = digit_count(second_year)

if first_year < second_year and count1 == count2 == 4:
    print(f'\nYears from {first_year} to {second_year} with '
          f'tree identical digits:')
    for year in range(first_year, second_year + 1):
        n1 = year // 1000
        n2 = year // 100 % 10
        n3 = year // 10 % 10
        n4 = year % 10
        if n1 == n2 == n3 or n1 == n2 == n4 or n1 == n3 == n4 or \
                n2 == n3 == n4:
            print(year)
else:
    print('Enter correct years')