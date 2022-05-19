# -*- coding: utf-8 -*-

# Подсчитать статистику по буквам в романе Война и Мир.
# Входные параметры: файл для сканирования
# Статистику считать только для букв алфавита (см функцию .isalpha() для строк)
#
# Вывести на консоль упорядоченную статистику в виде
# +---------+----------+
# |  буква  | частота  |
# +---------+----------+
# |    А    |   77777  |
# |    Б    |   55555  |
# |   ...   |   .....  |
# |    a    |   33333  |
# |    б    |   11111  |
# |   ...   |   .....  |
# +---------+----------+
# |  итого  | 9999999  |
# +---------+----------+
#
# Упорядочивание по частоте - по убыванию. Ширину таблицы подберите по своему вкусу
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.

# TODO здесь ваш код
import os.path
import zipfile


class MakeStat:
    def __init__(self, path):
        self.file_name = path

    def _unzip(self):
        zfile = zipfile.ZipFile(file=self.file_name, mode='r')
        for filename in zfile.namelist():
            zfile.extract(filename)
        return filename

    def _make_letters_dict(self, filename):
        if filename.endswith('.zip'):
            filename = self._unzip()
        with open(filename, 'r') as file:
            letters_dict = {}
            for line in file:
                for char in line:
                    if char.isalpha():
                        if char in letters_dict:
                            letters_dict[char] += 1
                        else:
                            letters_dict[char] = 1
        return letters_dict

    def make_sorted_letters_list(self, way_to_sort):
        letters_list = []
        way_to_sort = int(way_to_sort)
        for letter, count in self._make_letters_dict(self.file_name).items():
            letters_list.append([letter, count])
            if way_to_sort == 1:
                letters_list.sort(key=lambda i: i[1], reverse=True)
            elif way_to_sort == 2:
                letters_list.sort(key=lambda i: i[1], reverse=False)
            elif way_to_sort == 3:
                letters_list.sort(key=lambda i: i[0], reverse=False)
            elif way_to_sort == 4:
                letters_list.sort(key=lambda i: i[0], reverse=True)
        return letters_list

    def print_stat(self, stat_list):
        print('''+---------+----------+
|  буква  | частота  |
+---------+----------+''')
        for letter_stat in stat_list:
            print(f'|{letter_stat[0]:^9}|{letter_stat[1]:^10}|')
        total = 0
        for letter_stat in stat_list:
            total += letter_stat[1]
        print(f'''+---------+----------+
|  итого  |{total:^10}|
+---------+----------+''')


# path = 'D:\\courses\\IT\\Python\\SkillBox_Python\\Practice\\lesson_009\\python_snippets\\voyna-i-mir.txt.zip'
path = input('Введите путь:\n')
# file = r'os.path.normpath(path)'
# print(path)

make_stat = MakeStat(path=path)
letters_list = make_stat.make_sorted_letters_list(4)
make_stat.print_stat(letters_list)

# После выполнения первого этапа нужно сделать упорядочивание статистики
#  - по частоте по возрастанию
#  - по алфавиту по возрастанию
#  - по алфавиту по убыванию
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
