def add_contact(some_dict):
    name = input('\nВведите имя: ').lower()
    surname = input('Введите фамилию: ').lower()
    mobile_number = input('Введите мобильный телефон: ')
    if (name, surname) in some_dict:
        print('Контакт уже есть в списке.')
    some_dict[name, surname] = mobile_number


def search_contact(some_dict):
    enter_surname = input('\nВведите фамилию человека: ').lower()
    for name_surname, mob_num in some_dict.items():
        name, surname = name_surname
        if surname == enter_surname:
            print(f'Контакт {name_surname} найден. Номер телефона {mob_num}')


generate_dict = dict()
while True:
    add_contact_or_search_contact = input('"добавить контакт" или "найти контакт" или "стоп": ')
    if add_contact_or_search_contact == 'добавить контакт':
        print(add_contact(generate_dict))
    elif add_contact_or_search_contact == 'найти контакт':
        print(search_contact(generate_dict))
    elif add_contact_or_search_contact == 'стоп':
        break
    else:
        print('Ошибка выбора')
