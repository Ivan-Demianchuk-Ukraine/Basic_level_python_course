# 1. Создать класс Employee содержащий следуюущие свойства:
#     'firstname': 'Ivasik',
#     'lastname': 'Telesik',
#     'age': 13,
#     'e-mail': 'ivasik-telesik1732@izkurnanog.ua',
#     'skills': ['ходить', "говорить", "кодить"],
#     'people_lang': ['Україньська', "Англійська"],
#     'coding_lang': ['Python', "C++", "lisp"],


# методы добавить на свое усмотрение(удобство нужно)
# добавить метод записи данных сотрудника в файл(JSON/CSV)
# *добавить метод создания объекта сотрудника на основании файла
# *2. Создать класс Employer содержащий следующие свойства:
#     'name': 'Roga i kopita',
#     'address':'some address'
#     'employees': []
# должны присутствовать методы добавления/удаления сотрудников
# методы записи/чтения сотрудников в/из файла

class Employee:
    def __init__(self, firstname, lastname, age, email, skills, people_lang, coding_lang):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.email = email
        self.skills = skills
        self.people_lang = people_lang
        self.coding_lang = coding_lang


class Employer:
    def __init__(self, name, address, employees):
        self.name = name
        self.address = address
        self.employees = employees


employee = Employee('Ivasik', 'Telesik', 13, 'ivasik-telesik1732@izkurnanog.ua', ['ходить', "говорить", "кодить"],
                    ['Україньська', "Англійська"], ['Python', "C++", "lisp"])

hillel_company = Employer('Roga i kopita', 'some address', [])
