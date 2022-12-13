# 1)У вас есть строка my_string = '0123456789'.
# Сгенерировать целые числа (тип int) от 0 до 99 и распечатать их.
# Задание нужно выполнить ТОЛЬКО через цикл в цикле(См. пример выше) и приведение типов.
# Генерирование через range или другие "фишки" я засчитывать не буду ))


count = 0
result_string = ''
while count < 100:
    print(count+1)
    count = count + 1
    result_string = result_string + str(count)
print(result_string)




# При помощи вложенных циклов (можно while, можно for) нарисовать следующие фигуры
# представленные ниже. Пользователь вводит, с клавиатуры, высоту фигуры в символах.
high = int(input('Enter the high: '))
space = ' '
print(space * high, '*')
count = high
spaces_between_stars = 3
for i in range(high - 2):
    count -= 1
    print(space * count, '*', space * spaces_between_stars, '*', sep='')
    spaces_between_stars += 2
print('* ' * int((spaces_between_stars/2) + 3), sep='')
# A
#             *
#           *   *
#         *       *
#       *           *
#     *               *
#   *                   *
# * * * * * * * * * * * * *


high = int(input('Enter the high: '))
space = ' '
print(space * high, '*')
count = high
spaces_between_stars = 3
for i in range(high - 2):
    count -= 1
    print(space * count, '* ', '* ' * (int(spaces_between_stars/2)), '*', sep='')
    spaces_between_stars += 2
print('* '*int((spaces_between_stars/2) + 3), sep='')

# B
#             *
#           * * *
#         * * * * *
#       * * * * * * *
#     * * * * * * * * *
#   * * * * * * * * * * *
# * * * * * * * * * * * * *


high = int(input('Enter the high: '))
space = ' '
print(space * high, '*')
count = high
spaces_between_stars = 3
for i in range(high - 2):
    count -= 1
    print(space*count, '* ', '* '*(int(spaces_between_stars/2)), '*', sep='')
    spaces_between_stars += 2
print('* ' * int((spaces_between_stars/2) + 3), sep='')
count = 0
for i in range(high - 2):
    count += 1
    print(space * count, '*', space * spaces_between_stars, '*', sep='')
    spaces_between_stars -= 2
print(space * high, '*')
# C
#             *
#           * * *
#         * * * * *
#       * * * * * * *
#     * * * * * * * * *
#   * * * * * * * * * * *
# * * * * * * * * * * * * *
#   *                   *
#     *               *
#       *           *
#         *       *
#           *   *
#             *


high = int(input('Enter the high: '))
space = ' '
print(space * high, '*')
count = high
spaces_between_stars = 3
for i in range(high - 2):
    count -= 1
    print(space * count, '* ', '* '*(int(spaces_between_stars/2)), '*', sep='')
    spaces_between_stars += 2
print('* ' * int((spaces_between_stars/2) + 3), sep='')
count = 0
for i in range(high - 2):
    if spaces_between_stars % 2 != 0:
        half_spaces_between_stars = spaces_between_stars // 2
        count += 1
        print(space * count, '*', space * half_spaces_between_stars, '*', space*half_spaces_between_stars, '*', sep='')
        spaces_between_stars -= 2
    else:
        count += 1
        print(space * count, '*', space * spaces_between_stars, '*', sep='')
        spaces_between_stars -= 2
print(space * high, '*')

# D
#             *
#           * * *
#         * * * * *
#       * * * * * * *
#     * * * * * * * * *
#   * * * * * * * * * * *
# * * * * * * * * * * * * *
#   *         *         *
#     *       *       *
#       *     *     *
#         *   *   *
#           * * *
#             *
# *
