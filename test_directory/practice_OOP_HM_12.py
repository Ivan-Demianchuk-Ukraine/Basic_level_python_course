import os

# Написать метод класса, который получает имя директории и словарь по примеру из задания 1.
# Функция проверяет соответствие полученного словаря и реальной файловой системы в полученной папке и,
# если надо, создает нужные папки и пустые файлы, в соответствии со структурой словаря.
# Пример:
# создали на основании данных в папке -> {'filenames': [файл1, файл2, файл7], 'dirnames': [папка1, папка2]}
# передали в метод -> {'filenames': [файл1, файл7, файл13], 'dirnames': [папка11, папка2]}
# в результате необходимо создать файл13 и папка11


class WithFile:
    files = []
    folders = []

    def __init__(self, dir_name: str):
        """
        Constructor for WithFile class
        param dir_name: name of the directory
        """

        self.dir_name = dir_name
        self.dict = None

    def create_dict(self):
        """
        Creates a dictionary of files and folders in the directory

        return: string representation of the files and folders in the directory
        """
        path_to = os.getcwd()
        list_of_files_or_folders = os.listdir(r'C:\Users\PREDATOR\PycharmProjects\basic_python_course\test_directory')
        for i in list_of_files_or_folders:
            if os.path.isfile(path_to + f'\\{i}'):
                self.files.append(i)
            else:
                self.folders.append(i)
        self.dict = {'filenames': self.files, 'dirnames': self.folders}
        return f'files: {self.files} and folders: {self.folders}'

    def order_dict(self, bool_value: bool):
        """
        Orders the files and folders in the dictionary in ascending or descending order based on the input boolean value

        param bool_value: True for ascending order, False for descending order
        return: the ordered dictionary of files and folders
        """
        if bool_value:
            self.dict['filenames'] = sorted(self.dict['filenames'])
            self.dict['dirnames'] = sorted(self.dict['dirnames'])
            return self.dict
        elif not bool_value:
            self.dict['filenames'] = sorted(self.dict['filenames'], reverse=True)
            self.dict['dirnames'] = sorted(self.dict['dirnames'], reverse=True)
            return self.dict

    def add_file_or_folder(self, string: str) -> dict:
        """
        Adds file or folder to the corresponding list. And creates this file/folder in the current directory.
        :param: receiving any string value. If it will be file name, then there must be dot in the name.
         If folder then without dot.
        :return:
        """
        if '.' in string:
            self.files.append(string)
            self.dict['filenames'] = self.files
            with open(string, 'w'):
                pass
            return self.dict
        else:
            self.folders.append(string)
            self.dict['dirnames'] = self.folders
            with open(string, 'w'):
                pass
            return self.dict


instance = WithFile('test_directory')
print('your created dict: ', instance.create_dict())
print(instance.add_file_or_folder('json.txt'))
print(instance.add_file_or_folder('folder2'))
print(instance.order_dict(False))
