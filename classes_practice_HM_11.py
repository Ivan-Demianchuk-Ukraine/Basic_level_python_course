import json


class Employee:
    def __init__(self, firstname, lastname, age, email, skills, people_lang, coding_lang):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.email = email
        self.skills = skills
        self.people_lang = people_lang
        self.coding_lang = coding_lang

    def __str__(self):
        return f'{self.firstname} {self.lastname}'

    def write_in_json(self):
        with open(f'employee info', 'w') as file:
            json_string = json.dumps(self.__dict__)
            file.writelines(json_string)

    def birth_year(self):
        return

    def rename(self, new_name: str, new_lastname: str):
        self.firstname = new_name
        self.lastname = new_lastname
        with open(f'employee info', 'a') as file:
            json_string = json.dumps(self.__dict__)
            file.writelines(json_string)
        return 'FirstName and LastName were changed.'


class Employer:
    def __init__(self, name: str, address: str, employees: list):
        self.name = name
        self.address = address
        self.employees = employees

    def get_info(self):
        return f'{self.name},{self.address}, {self.employees}'

    def change_address(self, new_address: str) -> str:
        old_address = self.address
        self.address = new_address
        return f'{old_address} was changed from on {new_address}'

    def hire_employee(self, employee_name) -> str:
        self.employees.append(employee_name.__str__())
        return f'{employee_name.firstname} {employee_name.lastname} was added in your company'

    def fire_employee(self, employee_name) -> str:
        self.employees.remove(employee_name.__str__())
        return f'{employee_name.firstname} {employee_name.lastname} was removed from your company'

    def write_in_json(self):
        with open(f'company_employees', 'w') as file:
            json_string = json.dumps(self.__dict__)
            file.writelines(json_string)

    @staticmethod
    def read_from_json():
        with open(f'company_employees', 'r') as file:
            return file.readlines()


employee = Employee('Ivasik', 'Telesik', 13, 'ivasik-telesik1732@izkurnanog.ua', ['walking', "speaking", "coding"],
                    ['ukr', "eng"], ['Python', "C++", "lisp"])

hillel_company = Employer('Roga i kopita', 'some address', [])

print(employee.rename('Olesik', 'Melesik'))
print(employee.firstname, employee.lastname)
print(hillel_company.change_address('Dnipro'))
print(hillel_company.hire_employee(employee))
print(hillel_company.get_info())

employee2 = Employee('Anton', 'Rahmed', 24, 'telepuzik@gmail.com', ['walking', "speaking", "coding"],
                    ['ukr', "eng"], ['Python', "C++", "lisp"])
print(hillel_company.hire_employee(employee2))
print(hillel_company.get_info())
print(hillel_company.fire_employee(employee))
print(hillel_company.get_info())
print(hillel_company.write_in_json())
print(hillel_company.read_from_json())
