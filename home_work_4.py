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
users_heigh = int(input('Enter the high: '))
space = ' '
print(space*users_heigh,'*')
count = users_heigh
spaces_between_stars = 3
for i in range(users_heigh-2):
    count -= 1
    print(space*(count),'*',space*(spaces_between_stars),'*', sep='')
    spaces_between_stars +=2
print('* '*int((spaces_between_stars/2) + 3), sep='')
# A
#             *
#           *   *
#         *       *
#       *           *
#     *               *
#   *                   *
# * * * * * * * * * * * * *


users_heigh = int(input('Enter the high: '))
space = ' '
print(space*users_heigh,'*')
count = users_heigh
spaces_between_stars = 3
for i in range(users_heigh-2):
    count -= 1
    print(space*(count),'* ','* '*(int(spaces_between_stars/2)),'*', sep='')
    spaces_between_stars +=2
print('* '*int((spaces_between_stars/2) + 3), sep='')

# B
#             *
#           * * *
#         * * * * *
#       * * * * * * *
#     * * * * * * * * *
#   * * * * * * * * * * *
# * * * * * * * * * * * * *


users_heigh = int(input('Enter the high: '))
space = ' '
print(space*users_heigh,'*')
count = users_heigh
spaces_between_stars = 3
for i in range(users_heigh-2):
    count -= 1
    print(space*(count),'* ','* '*(int(spaces_between_stars/2)),'*', sep='')
    spaces_between_stars +=2
print('* '*int((spaces_between_stars/2) + 3), sep='')
count = 0
for i in range(users_heigh-2):
    count += 1
    print(space*(count),'*',space*(spaces_between_stars),'*', sep='')
    spaces_between_stars -=2
print(space*users_heigh,'*')
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


users_heigh = int(input('Enter the high: '))
space = ' '
print(space*users_heigh,'*')
count = users_heigh
spaces_between_stars = 3
for i in range(users_heigh-2):
    count -= 1
    print(space*(count),'* ','* '*(int(spaces_between_stars/2)),'*', sep='')
    spaces_between_stars +=2
print('* '*int((spaces_between_stars/2) + 3), sep='')
count = 0
for i in range(users_heigh-2):
    if spaces_between_stars % 2 != 0:
        bount_new = spaces_between_stars // 2
        count += 1
        print(space * (count), '*', space * (bount_new), '*', space * (bount_new), '*', sep='')
        spaces_between_stars -= 2
    else:
        count += 1
        print(space*(count),'*',space*(spaces_between_stars),'*', sep='')
        spaces_between_stars -=2
print(space*users_heigh,'*')

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


