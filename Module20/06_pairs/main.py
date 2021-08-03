original_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(f'Первое способ: {list(tuple(zip(original_list[::2], original_list[1::2])))}')

new_list = []
s = tuple()
for i in original_list:
    if i % 2 == 0:
        new_list.append((i, i + 1))

print(f'Второй способ: {new_list}')

new_list_2 = [(i, i + 1)for i in original_list if i % 2 == 0]

print(f'Третий способ: {new_list_2}')