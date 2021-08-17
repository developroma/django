score_table = {}
number_rows = int(input('Общее количество строк протокола: '))
print('Введите результат - имя участника (через пробел):')
for time in range(number_rows):
    ball, name = input('{0} запись: '.format(time + 1)).split()
    ball = int(ball)
    if name in score_table:
        score_table[name] = ball
    else:
        score_table[name] = ball
s = sorted(score_table.values(), reverse=True)
s2 = score_table.keys()

for i2 in s2:
    for i in s:
        if score_table[i2] == i:
            print(i2)