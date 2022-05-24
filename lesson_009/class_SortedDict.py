# Клевую таску придумал
# Напиши свой класс
# SortedDictionary
# Который будет реализацией словаря, который хранит порядок)
# По идее это не сложно
# У тебя под капотом будет простой словарь с парой методов сортировки, которые будут спрятаны
# Задача - что бы у тебя твой сортедДикт мог сортировать по ключам, значения, возрастанию и убыванию
# Сможешь сделать?

class SortedDictionary:

    def __init__(self, dict_to_sort):
        self.dict_to_sort = dict_to_sort

    def sort_dict_by_key(self, reverse=False):
        def make_keys_list():
            keys_list = list(self.dict_to_sort.keys())
            return keys_list

        def sort_key_list():
            sorting_key_list = make_keys_list()
            sorting_key_list.sort(reverse=reverse)
            return sorting_key_list

        sorted_key_list = sort_key_list()
        print('{', end='')
        for key in sorted_key_list:
            value = self.dict_to_sort[key]
            print(f"'{key}': {value}, ", end='')
        print('}')


my_dict = {
    'd': [1, 4],
    'b': 2,
    'c': 3
}
print(my_dict)
print(type(my_dict))
print('')
sorted_dict = SortedDictionary(my_dict)
sorted_dict.sort_dict_by_key()
print(type(sorted_dict))
my_dict.keys()
