# -*- coding: utf-8 -*-

# (цикл while)

# даны целые положительные числа a и b (a > b)
# Определить результат целочисленного деления a на b, с помощью цикла while,
# __НЕ__ используя стандартную операцию целочисленного деления (// и %)
# Формат вывода:
#   Целочисленное деление ХХХ на YYY дает ZZZ

a, b = 179, 37

# TODO здесь ваш код
remainder = a
result = 0
while remainder > b:
    remainder -= b
    result += 1
    pass
print('Целочисленное деление', a, 'на', b, 'дает', result)