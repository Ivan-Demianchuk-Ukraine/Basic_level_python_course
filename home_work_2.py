# 1. n школьников делят k яблок поровну, неделящийся остаток остается в корзинке.
# Сколько яблок достанется каждому школьнику?
#  Сколько яблок останется в корзинке?
#  Программа получает на вход числа `n` и `k` и должна вывести искомое количество яблок (два числа)

# students = 3
# apples = 4
# apples_per_student = apples / students
# apples_remains = apples_per_student - int(apples_per_student)
# print(int(apples_per_student))
# print(apples_remains)


# 2. В школе решили набрать три новых математических класса. Так как занятия по математике у них проходят
# в одно и то же время, было решено выделить кабинет для каждого класса и купить в них новые парты.
# За каждой партой может сидеть не больше двух учеников. Известно количество учащихся в каждом из трёх классов.
# Сколько всего нужно закупить парт чтобы их хватило на всех учеников?
# Программа получает на вход три натуральных числа: количество учащихся в каждом из трех классов.
a = 11
b = 23
c = 35
class_a = a // 2
class_a_left = a % 2
class_b = b // 2
class_b_left = b % 2
class_c = c // 2
class_c_left = c % 2
aa = class_a + class_a_left
bb = class_b + class_b_left
cc = class_c + class_c_left
print(aa, bb, cc)



# 3. Дано целое, положительное, трёхзначное число. Например: 123, 867, 374.
# Необходимо его перевернуть. Например, если ввели число 123,
#  то должно получиться на выходе ЧИСЛО 321. ВАЖНО! Работать только с числами. Строки использовать НЕЛЬЗЯ!

# number = int(input('Your Number: '))
# second_and_third_digit = number % 100
# first_letter = second_and_third_digit % 10
# second_letter = second_and_third_digit // 10
# third_letter = number // 100
# print(first_letter, second_letter, third_letter, sep='')

# Микропроцессор электронных часов считает количество секунд прошедших от начала суток
# (значение вводится с клавиатуры пользователем). Необходимо написать программу отображающую время
#  в формате чч:мм:сс. Например: 9375 -> 2:36:15


# a = int(input())
# in_minutes = (int(a) / 60)
# print(in_minutes)
# in_hours = int(in_minutes / 60)
# print(in_hours)
# remaining_minutes = int(in_minutes - (in_hours*60))
# print(remaining_minutes)
# minutes_and_seconds = in_minutes - (in_hours*60)
# print(minutes_and_seconds)
# remaining_seconds_2 = int((minutes_and_seconds - int(minutes_and_seconds)) * 60)
# print(f'{in_hours}:{remaining_minutes}:{remaining_seconds_2}')
