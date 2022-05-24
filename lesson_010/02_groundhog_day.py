# -*- coding: utf-8 -*-

# День сурка
#
# Напишите функцию one_day() которая возвращает количество кармы от 1 до 7
# и может выкидывать исключения:
# - IamGodError
# - DrunkError
# - CarCrashError
# - GluttonyError
# - DepressionError
# - SuicideError
# Одно из этих исключений выбрасывается с вероятностью 1 к 13 каждый день
#
# Функцию оберните в бесконечный цикл, выход из которого возможен только при накоплении
# кармы до уровня ENLIGHTENMENT_CARMA_LEVEL. Исключения обработать и записать в лог.
# При создании собственных исключений максимально использовать функциональность
# базовых встроенных исключений.
from random import randint

ENLIGHTENMENT_CARMA_LEVEL = 777


# TODO здесь ваш код
def one_day():
    error_n = randint(0, 7)
    dice = randint(1, 14)
    karma = randint(1, 7)
    errors = ['IamGodError', 'DrunkError', 'CarCrashError', 'GluttonyError', 'DepressionError', 'SuicideError']
    if dice == 1:
        raise BaseException(errors[error_n])
    return karma


# https://goo.gl/JnsDqu
current_karma = 0
exceptions = []
while current_karma <= ENLIGHTENMENT_CARMA_LEVEL:
    try:
        current_karma += one_day()
    except BaseException as exc:
        exceptions.append(str(exc))

print(exceptions)
