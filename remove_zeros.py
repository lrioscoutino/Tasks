def remove_any_value(the_list, val):
    return [value for value in the_list if value != val]


if __name__ == '__main__':
    list_1 = [2, 4, 0, 0, 0, 0, 4, 3, 4, 1, 2, 3]
    list_result = remove_any_value(list_1, 0)
    print(list_result)
