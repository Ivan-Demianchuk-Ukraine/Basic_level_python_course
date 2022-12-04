# 1. Написать калькулятор для простых операций(+,-,*,/,**),
# Операнды и оператор вводятся с клавиатуры отдельно(отдельные переменные)
# first_number = int(input('Enter your first number '))
# operator = str(input('Enter operator: '))
# second_number = int(input('Enter your second number '))
#
#
# if operator == '+':
#     print(first_number + second_number)
#
# elif operator == '-':
#     print(first_number - second_number)
#
# elif operator == '*':
#     print(first_number * second_number)
#
# elif operator == '/':
#     print(first_number / second_number)
#
# elif operator == '**':
#     print(first_number ** second_number)



# 2. По данному целому числу N распечатайте все квадраты натуральных чисел,
#  не превосходящие N, в порядке возрастания.
# Например:
# 50      1 4 9 16 25 36 49
# 10      1 4 9
# 100     1 4 9 16 25 36 49 64 81 100
# number = int(input('Enter your number: '))
# for i in range(1, number):
#     if i ** 2 <= number:
#         print(i ** 2, end=' ')


# 3. Определить является ли введенное с клавиатуры число простым
# (делится без остатка только на себя и единицу)
enter = int(input('Enter your number: '))
if enter / 1 == enter and enter % 2 == True and enter != 1 and enter != -1 and enter % 3 != 0 and enter % 5 != 0 and enter % 7 != 0 and enter % 9 != 0:
    print('YES! This is prime number.')
elif enter == 3 or enter == 7 or enter == 5:
    print('YES! This is prime number.')
elif enter == 9:
    print('No! This is not prime number')
elif enter == 1 or enter == -1:
    print('Wrong number')
else:
    print('NO! This is not prime number')


# *(НЕОБЯЗАТЕЛНО! НА ОЦЕНКУ НЕ ВЛИЯЕТ)
# Создайте приложение подбирающее правильное окончание к фразе:
#  "Маша нашла в лесу {К} гриб...". K пользователь вводит с клавиатуры.
# Например: Маша нашла в лесу 7 грибОВ.
# Маша нашла в лесу 32 грибА.

