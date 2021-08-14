amount = int(input('Сколько записей вносится в протокол? '))
# if amount < 3:
#     print('Участников не может быть меньше 3х:')

print('Записи (результат и имя)')

generate_dict = dict()

for i in range(amount):
    exp, name = input(f'{i + 1} запись: ').split()
    if name in generate_dict:
        max_one = max(exp)
        generate_dict[name] = max_one
    else:
        generate_dict[name] = exp

values_list = [int(values) for values in generate_dict.values()]
keys_list = [keys for keys in generate_dict.keys()]

exp_list = sorted(values_list, reverse=True)
three_winners = exp_list[:3]

sorted_keys_list = sorted(keys_list)
print(sorted_keys_list)
