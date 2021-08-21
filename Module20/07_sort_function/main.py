def func(tup):
    list_tup = list(tup)
    for i in range(len(list_tup)):
        for curr in range(i, len(list_tup)):
            if list_tup[i] > list_tup[curr]:
                list_tup[curr], list_tup[i] = list_tup[i], list_tup[curr]
    return tuple(list_tup)


result = func((2, 5, 6, 1, 6, 7))
print(result)