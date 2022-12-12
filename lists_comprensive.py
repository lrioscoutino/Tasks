# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def lists_comprensive():
    list_1 = [1, 2, 5, 6, 8, 9 , 10, 11]
    list_2 = [3, 4, 5, 9, 10]
    list_result = [el for el in list_1 if el in list_2]
    return list_result


if __name__ == '__main__':
    list_result = lists_comprensive()
    print(list_result)
