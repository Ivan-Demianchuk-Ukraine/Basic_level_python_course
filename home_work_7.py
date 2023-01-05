# 1)Дан список словарей persons в формате [{"name": "John", "age": 15}, ... ,{"name": "Jack", "age": 45}]
import statistics
persons = [{"name": "John", "age": 15}, {"name": "Jacks", "age": 15}, {"name": "Rex", "age": 30}]

# #     а) Создать список и поместить туда имя самого молодого человека.
# #         Если возраст совпадает - поместить все имена самых молодых.

# lst_youngest_person = []
#
# ages = []
# for i in persons:
#     ages.append(i['age'])
# min_ages = min(ages)
#
# for i in persons:
#     if i['age'] == min_ages:
#         print(i['age'])
#         lst_youngest_person.append(i)
# print(lst_youngest_person)

# б) Создать список и поместить туда самое длинное имя. Если длина имени совпадает - поместить все такие имена.
# lst_longest_name = []
# names = []
# for i in persons:
#     names.append(len(i['name']))
# max_longest_name = max(names)
# names = [i for i in persons if len(i['name']) == max_longest_name]
# print(names)


# в) Посчитать среднее количество лет всех людей из начального списка.
# ages = []
# for i in persons:
#     ages.append(i['age'])
# print(statistics.mean(ages))




# 2)Даны два словаря my_dict_1 и my_dict_2.
my_dict_1 = {'Product': "Milk", "tasty": 'bad', 'Description': 'some text', 'Size': '1 L'}
my_dict_2 = {'Product': "Juice", "tasty": 'good', 'Guarantee': 'yes'}

# а) Создать список из ключей, которые есть в обоих словарях.
# keys_lst = [my_dict_1.keys(), my_dict_2.keys()]
# print(keys_lst)


# б) Создать список из ключей, которые есть в первом, но нет во втором словаре.
# keys_lst = []
# for i in my_dict_1:
#     if i not in my_dict_2:
#         keys_lst.append(i)
#     else:
#         pass
# print(keys_lst)

# в) Создать новый словарь из пар {ключ:значение}, для ключей, которые есть в первом, но нет во втором словаре.
# my_dict_3 = {}
# for i in my_dict_1:
#     if i not in my_dict_2:
#         my_dict_3.update({i: my_dict_1.get(i)})
#     else:
#         pass
# print(my_dict_3)


#     г) Объединить эти два словаря в новый словарь по правилу:
#         если ключ есть только в одном из двух словарей - поместить пару ключ:значение,
#         если ключ есть в двух словарях -
#         поместить пару {ключ: [значение_из_первого_словаря, значение_из_второго_словаря]},
#         {1:1, 2:2}, {11:11, 2:22} ---> {1:1, 11:11, 2:[2, 22]}

# my_dict_3 = {}
# for i in my_dict_1:
#     if i not in my_dict_2:
#         my_dict_3.update({i: my_dict_1.get(i)})
#     elif i in my_dict_2:
#         my_dict_3.update({i: [my_dict_1.get(i), my_dict_2.get(i)]})
#     else:
#         pass
# print(my_dict_3)
