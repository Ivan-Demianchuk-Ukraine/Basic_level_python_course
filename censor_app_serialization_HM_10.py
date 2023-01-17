import json
import csv


def censor(file_name, lst_words):
    file = open(f'{file_name}', 'r')
    opened_file = file.read()
    split_opened_file = opened_file.split()
    words_with_count = {}
    for _ in split_opened_file:

        if _.isalpha() and _ not in words_with_count:
            words_with_count[str(_)] = str(split_opened_file.count(_))

    with open('stat.json', 'w') as json_file:
        json_string = json.dumps(words_with_count)
        json_file.writelines(json_string)
    print('Json - ', words_with_count)

    words_list_for_csv = []
    for i in words_with_count:
        words_list_for_csv.append(i + '-' + words_with_count[i])
    print('CSV - ', words_list_for_csv)

    with open('stat.csv', 'w') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(words_list_for_csv)

    for i in lst_words:
        opened_file = opened_file.replace(i, '*' * len(i))
    print('-' * 5, ' Text after Censor: ', '-' * 5, '\n', opened_file, sep='')
    file.close()


censor('newfile.txt', ['war', 'string'])
