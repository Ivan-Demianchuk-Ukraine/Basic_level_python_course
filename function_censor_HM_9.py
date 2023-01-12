# Написать функцию цензор. На вход функция получает имя файла и список слов для замены,
# функция ничего не возвращает, но в результате ее работы необходимо создать файл,
# в котором слова из списка заменены шаблоном(звездочками например)
def censor(file_name, lst_words):
    file = open(f'{file_name}.txt', 'r')
    opened_file = file.read()
    for i in lst_words:
        opened_file = opened_file.replace(i, '*' * len(i))
    print(opened_file)
    file.close()


censor('newfile', ['war', 'string'])
