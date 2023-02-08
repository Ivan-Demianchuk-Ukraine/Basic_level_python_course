import os


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
        list_of_files_or_folders = os.listdir()
        for i in list_of_files_or_folders:
            if os.path.isfile(path_to + f'\\{i}'):
                self.files.append(i)
            else:
                self.folders.append(i)
        self.dict = {'filenames': self.files, 'dir-names': self.folders}
        return f'files: {self.files} and folders: {self.folders}'

    def order_dict(self, bool_value: bool):
        """
        Orders the files and folders in the dictionary in ascending or descending order based on the input boolean value

        param bool_value: True for ascending order, False for descending order
        return: the ordered dictionary of files and folders
        """
        if bool_value:
            self.dict['filenames'] = sorted(self.dict['filenames'])
            self.dict['dir-names'] = sorted(self.dict['dir-names'])
            return self.dict
        elif not bool_value:
            self.dict['filenames'] = sorted(self.dict['filenames'], reverse=True)
            self.dict['dir-names'] = sorted(self.dict['dir-names'], reverse=True)
            return self.dict

    def add_file_or_folder(self, file_or_folder_name: str) -> dict:
        """
        Adds file or folder to the corresponding list. And creates this file/folder in the current directory.
        :param: receiving any string value. If it will be file name, then there must be dot in the name.
         If folder then without dot.
        :return:
        """
        if '.' in file_or_folder_name:
            self.files.append(file_or_folder_name)
            self.dict['filenames'] = self.files
            with open(file_or_folder_name, 'w'):
                pass
            return self.dict
        else:
            self.folders.append(file_or_folder_name)
            self.dict['dir-names'] = self.folders
            with open(file_or_folder_name, 'w'):
                pass
            return self.dict


instance = WithFile('test_directory')
print('your created dict: ', instance.create_dict())
print(instance.add_file_or_folder('json.txt'))
print(instance.add_file_or_folder('folder2'))
print(instance.order_dict(False))
