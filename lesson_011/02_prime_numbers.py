# -*- coding: utf-8 -*-


# Есть функция генерации списка простых чисел


def get_prime_numbers(n):
    prime_numbers = []
    for possible_prime in range(2, n + 1):
        is_prime = True
        a = int(possible_prime ** 0.5) + 1
        for num in range(2, a):
            if possible_prime % num == 0:
                is_prime = False
                break
        if is_prime:
            prime_numbers.append(possible_prime)
    return prime_numbers


# Часть 1
# На основе алгоритма get_prime_numbers создать класс итерируемых объектов,
# который выдает последовательность простых чисел до n
#
# Распечатать все простые числа до 10000 в столбик

class PrimeNumbers:

    def __init__(self, n, i=0):
        self.i = i
        self.number_list = get_prime_numbers(n)
        self.n = n

    def __iter__(self):
        self.i = 0
        return self

    def __next__(self):
        self.i += 1
        if self.i <= self.n:
            return self.number_list[self.i - 1]
        else:
            raise StopIteration


# print(get_prime_numbers(10000))

# prime_number_iterator = PrimeNumbers(n=10000)
# for number in prime_number_iterator:
#     print(number)


# TODO после подтверждения части 1 преподавателем, можно делать
# Часть 2
# Теперь нужно создать генератор, который выдает последовательность простых чисел до n
# Распечатать все простые числа до 10000 в столбик


def prime_numbers_generator(n):
    nums = get_prime_numbers(n)
    while nums:
        next_num = nums.pop(0)
        yield next_num

    # TODO здесь ваш код


# for number in prime_numbers_generator(n=10000):
#     print(number)

# Часть 3
# Написать несколько функций-фильтров, которые выдает True, если число:
# 1) "счастливое" в обыденном понимании - сумма первых цифр равна сумме последних
#       Если число имеет нечетное число цифр (например 727 или 92083),
#       то для вычисления "счастливости" брать равное количество цифр с начала и конца:
#           727 -> 7(2)7 -> 7 == 7 -> True
#           92083 -> 92(0)83 -> 9+2 == 8+3 -> True
# 2) "палиндромное" - одинаково читающееся в обоих направлениях. Например, 723327 и 101
# 3) придумать свою (https://clck.ru/GB5Fc в помощь)
#
# Подумать, как можно применить функции-фильтры к полученной последовательности простых чисел
# для получения, к примеру: простых счастливых чисел, простых палиндромных чисел,
# простых счастливых палиндромных чисел и так далее. Придумать не менее 2‑х способов.
#
# Подсказка: возможно, нужно будет добавить параметр в итератор/генератор.
def sum_num(numbers):
    sum_of_numbers = 0
    for number in numbers:
        sum_of_numbers += int(number)
    return sum_of_numbers


def cut_number(num):
    half_len = len(num) // 2
    num_begin = num[:half_len]
    num_end = num[-half_len:]
    return [num_begin, num_end]


def is_happy(num):
    number = str(num)
    if sum_num(cut_number(number)[0]) == sum_num(cut_number(number)[1]):
        return True
    else:
        return False


# for number in prime_numbers_generator(n=10000):
#     if is_happy(number):
#         print(number)
