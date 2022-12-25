# 3. Даны списки my_list_1 и my_list_2. Создать список my_result в который вначале поместить элементы на
# четных местах из
# my_list_1, а потом все элементы на нечетных местах из my_list_2.
# my_list_1 = ['a', 'b', 4, 'd', 'wd']
# my_list_2 = ['y', 'z', 6, 'g']
# my_result = []
# count = 0
# len_list_1 = len(my_list_1)
# len_list_2 = len(my_list_2)
#
# if len_list_1 > len_list_2:
#     for i in range(len_list_1 - len_list_2):
#         my_list_1.pop()
#         len_list_1 = len_list_2
# elif len_list_1 < len_list_2:
#     for i in range(len_list_2 - len_list_1):
#         my_list_2.pop()
#         len_list_2 = len_list_1
#
#
# while len(my_result) != len_list_1 + len_list_2:
#     my_result.append(my_list_2[count])
#     my_result.append(my_list_1[count])
#     count += 1
# print(my_result)

# *4. Дан список my_list. СОЗДАТЬ НОВЫЙ список new_list у которого первый элемент из my_list стоит на последнем месте.
#  Если my_list [1,2,3,4], то new_list [2,3,4,1]
# my_list = [1, 2, 3, 4]
# new_list = [i for i in my_list if i != my_list[0]]
# new_list.append(my_list[0])
# print(new_list)



# *5. Дан список my_list. В ЭТОМ списке первый элемент переставить на последнее место.[1,2,3,4] -> [2,3,4,1].
# Пересоздавать список нельзя! (используйте метод pop)
# my_list = [1, 2, 3, 4]
# my_list.append(my_list[0])
# my_list.pop(0)
# print(my_list)

# *6. Дана строка в которой есть числа (разделяются пробелами). Например "43 больше чем 34, но меньше чем 56".
# Найти сумму ВСЕХ ЧИСЕЛ (А НЕ ЦИФР) в этой строке. Для данного примера ответ - 133.
# (используйте split и проверку isdigit)

# my_str = '43 больше ч1)2ем 34)., но меньше чем 56'
# for i in my_str:
#     if i.isdigit():
#         pass
#     else:
#         my_str = my_str.replace(i, ' ')
#
# result = [int(i) for i in my_str.split() if i.isdigit()]
# print(sum(result))


# *7. Дана строка my_str в которой символы МОГУТ повторяться и два символа l_limit и r_limit, которые точно находятся в
# этой строке. Причем l_limit левее чем r_limit. В переменную sub_str поместить НАИБОЛЬШУЮ часть строки между этими
#  символами. my_str = "My long string", l_limit = "o", r_limit = "g" -> sub_str = "ng strin".
my_str = "My long string"
l_limit = "o"
r_limit = "g"
sub_str = "ng strin"

# *8. Дана строка my_str. Разделите эту строку на пары из двух символов и поместите эти пары в список. Если строка
#  содержит нечетное количество символов, пропущенный второй символ последней пары должен быть заменен
#  подчеркиванием ('_'). Примеры: 'abcd' -> ['ab', 'cd'], 'abcde' -> ['ab', 'cd', e_'](используйте срезы длинны 2)

# my_str = 'abcdefRs2'
# result = []
# timely_result = []
# count = 0
# if len(my_str) % 2 != 0:
#     my_str = my_str + '_'
# for i in my_str:
#     if len(timely_result) == 0:
#         timely_result.append(my_str[count] + my_str[count+1])
#         print(timely_result)
#         count += 2
#     else:
#         result.extend(timely_result)
#         timely_result.pop(0)
# print(result)

# *9. Дан список чисел. Определите, сколько в этом списке элементов, которые больше суммы двух своих соседей
#  (слева и справа), и НАПЕЧАТАЙТЕ КОЛИЧЕСТВО таких элементов. Крайние элементы списка никогда не учитываются,
#   поскольку у них недостаточно соседей. Для списка [2,4,1,5,3,9,0,7] ответом будет 3 потому что 4 > 2+1, 5 > 1+3, 9>3+0.
# lst_numbers = [2, 4, 1, 5, 3, 15, 9, 0, 7]
# count = 0
#
# for i in lst_numbers:
#     if i == lst_numbers[0] or i == lst_numbers[-1]:
#         print('this is first or last number')
#     elif i > lst_numbers[count] + lst_numbers[count+2]:
#         print(i, 'win')
#         count += 1
#     else:
#         count += 1

# *10. Дан список my_list в котором могут быть как строки (type str) так и целые числа (type int).
# Например [1, 2, 3, "11", "22", 33] Создать новый список в который поместить только строки из my_list.
# my_list = [1, 2, 3, "11", "22", 33, 's']
# result = [i for i in my_list if type(i) == str]
# print(result)

# 11. Дана строка my_str. Создать список в который поместить те символы из my_str, которые встречаются
# в строке ТОЛЬКО ОДИН раз.
# my_str = 'wdojowjd1zowd3ss5qpks'
# result = [i for i in my_str if my_str.count(i) == 1]
# print(result)

# *12. Даны две строки. Создать список в который поместить те символы,которые есть в обеих строках хотя бы раз.
# first_str = 'saqw2'
# second_str = 'sdd123qdd'
# result = [i for i in first_str if i in first_str and i in second_str]
# print(result)

# *13. Даны две строки. Создать список в который поместить те символы, которые есть в обеих строках, но в каждой
#  ТОЛЬКО ПО ОДНОМУ разу. Пример: для строк "aaaasdf1" и "asdfff2" ответ ["s", "d"],
#   т.к. эти символы есть в каждой строке по одному разу
# first_str = 'sadqw2'
# second_str = 's123qd'
# result = [i for i in first_str if first_str.count(i) == 1 and second_str.count(i) == 1]
# print(result)
