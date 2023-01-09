import random

def task_1(lst: list) -> list:
    new_list = []
    count = 1
    for i in lst:
        if count % 2 != 0 and isinstance(i, str):
            new_list.append(i[::-1])
            count += 1
        else:
            new_list.append(i)
            count += 1
    return new_list


def task_2(lst: list) -> list:
    new_list = []
    for i in lst:
        if type(i) != str:
            pass
        elif i[0] == 'a':
            new_list.append(i)

    return new_list


def task_3(lst: list) -> list:
    new_list = []
    for i in lst:
        if type(i) != str:
            pass
        elif 'a' in i or 'A' in i:
            new_list.append(i)

    return new_list


def task_4(lst: list) -> list:
    new_list = []
    for i in lst:
        if type(i) != str:
            pass
        else:
            new_list.append(i)

    return new_list


def task_5(string: str) -> list:
    new_lst = []
    for i in string:
        if string.count(i) == 1:
            new_lst.append(i)

    return new_lst


def task_6(string_1: str, string_2: str) -> list:
    new_lst = []
    for i in string_1:
        if i in string_1 and i in string_2:
            if i in new_lst:
                pass
            else:
                new_lst.append(i)

    return new_lst


def task_7(string_1: str, string_2: str) -> list:
    new_lst = []
    for i in string_1:
        if string_1.count(i) == 1 and string_2.count(i) == 1:
            new_lst.append(i)
    return new_lst


def get_random_string(length: int) -> str:
    c = ''
    for i in range(length):
        letters_or_digits = random.randint(1, 3)
        if letters_or_digits == 1:
            i = random.randint(48, 57)
            c = c + chr(i)
        elif letters_or_digits == 2:
            i = random.randint(65, 90)
            c = c + chr(i)
        elif letters_or_digits == 3:
            i = random.randint(97, 122)
            c = c + chr(i)
    return c


def task_8(names, domains):
    from random import randint
    number = randint(100, 999)
    len_names = len(names)
    len_domens = len(domains)
    name_random = names[randint(1, len_names) - 1]
    domen_random = domains[randint(1, len_domens) - 1]

    return f'{name_random}.{number}@{get_random_string(randint(5, 7))}{domen_random}'
