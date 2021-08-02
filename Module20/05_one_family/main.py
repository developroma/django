family_dict = {
    ('Сидоров', 'Никита'): 35,
    ('Сидорова', 'Алина'): 34,
    ('Сидоров', 'Павел'): 10,
    ('Зайцев', 'Афанасий'): 43,
    ('Соловьёв', 'Йоханес'): 21,
    ('Зайцева', 'Элла'): 23,
    ('Орлова', 'Юзефа'): 54,
    ('Орлов', 'Даниил'): 61,
    ('Никифоров', 'Станислав'): 27

}

input_surname = input('Введите фамилию: ').lower()

for name_surname, years in family_dict.items():
    surname = name_surname[0]
    surname = surname.lower()
    if surname.startswith(input_surname) or surname == input_surname[:-1]:
        for i in name_surname:
            print(i, end=' ')
        print(years)