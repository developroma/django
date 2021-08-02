def func(some_tuple, some_el):
    some_list = list(some_tuple)
    for i_list in some_list:
        new_list_first = i_list.find(some_el)
        quality_el = i_list.count(some_el)
        if quality_el >= 2:
            new_list_second = i_list.rfind(some_el)
            new_tuple = i_list[new_list_first:new_list_second + 1]

        elif quality_el == 1:
            new_tuple = i_list[new_list_first:]

        else:
            new_tuple = tuple()

        return tuple(new_tuple)


res = func(('error', ), 'r')
print(res)
