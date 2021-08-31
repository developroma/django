num = int(input('Введите число: '))


def func_range(num):
    num -= 1
    if num == 1:
        return 1
    print(func_range(num))
    return num


print(func_range(num+1))