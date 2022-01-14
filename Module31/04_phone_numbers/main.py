import re


telephone_list = ['9999999999', '999999-999', '99999x9999', '7999999999']

for i_num in telephone_list:
    if len(re.findall(r'\b[8,9]\d{9}\b', i_num)) > 0:
        print(telephone_list.index(i_num) + 1, 'номер: все в порядке')
    else:
        print(telephone_list.index(i_num) + 1, 'номер: не подходит')
