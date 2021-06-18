data = {
    ('Сидоров', 'Никита'): 35,
    ('Сидорова', 'Алина'): 34,
    ('Сидоров', 'Павел'): 10,
    ('Сидоровский', 'Игорь'): 9,
    ('Сидорож', 'Пшемек'): 25
}

input_surname = input('Enter surname: ')

for names, age in data.items():
    if (names[0].lower()[:len(input_surname)] == input_surname.lower()[:len(input_surname)]
            and abs(len(input_surname) - len(names[0])) <= 1):
        print(names[0], names[1], age)
