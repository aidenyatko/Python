# -*- coding: utf-8 -*-

# Игра «Быки и коровы»
# https://goo.gl/Go2mb9
#
# Правила:
# Компьютер загадывает четырехзначное число, все цифры которого различны
# (первая цифра числа отлична от нуля). Игроку необходимо разгадать задуманное число.
# Игрок вводит четырехзначное число c неповторяющимися цифрами,
# компьютер сообщают о количестве «быков» и «коров» в названном числе
# «бык» — цифра есть в записи задуманного числа и стоит в той же позиции,
#       что и в задуманном числе
# «корова» — цифра есть в записи задуманного числа, но не стоит в той же позиции,
#       что и в задуманном числе
#
# Например, если задумано число 3275 и названо число 1234,
# получаем в названном числе одного «быка» и одну «корову».
# Очевидно, что число отгадано в том случае, если имеем 4 «быка».
#
# Формат ответа компьютера
# > быки - 1, коровы - 1


# Составить отдельный модуль mastermind_engine, реализующий функциональность игры.
# В этом модуле нужно реализовать функции:
#   загадать_число()
#   проверить_число(NN) - возвращает словарь {'bulls': N, 'cows': N}
# Загаданное число хранить в глобальной переменной.
# Обратите внимание, что строки - это список символов.
#
# В текущем модуле (lesson_006/01_mastermind.py) реализовать логику работы с пользователем:
#   модуль движка загадывает число
#   в цикле, пока число не отгадано
#       у пользователя запрашивается вариант числа
#       модуль движка проверяет число и выдает быков/коров
#       результат быков/коров выводится на консоль
#  когда игрок угадал таки число - показать количество ходов и вопрос "Хотите еще партию?"
#
# При написании кода учитывайте, что движок игры никак не должен взаимодействовать с пользователем.
# Все общение с пользователем делать в текущем модуле. Представьте, что движок игры могут использовать
# разные клиенты - веб, чатбот, приложение, етс - они знают как спрашивать и отвечать пользователю.
# Движок игры реализует только саму функциональность игры.
# Это пример применения SOLID принципа (см https://goo.gl/GFMoaI) в архитектуре программ.
# Точнее, в этом случае важен принцип единственной ответственности - https://goo.gl/rYb3hT

# TODO здесь ваш код...
import os
import mastermind_engine
from termcolor import cprint

print('''# Правила:
# Компьютер загадывает четырехзначное число, все цифры которого различны
# (первая цифра числа отлична от нуля). Игроку необходимо разгадать задуманное число.
# Игрок вводит четырехзначное число c неповторяющимися цифрами,
# компьютер сообщают о количестве «быков» и «коров» в названном числе
# «бык» — цифра есть в записи задуманного числа и стоит в той же позиции,
#       что и в задуманном числе
# «корова» — цифра есть в записи задуманного числа, но не стоит в той же позиции,
#       что и в задуманном числе
#
# Например, если задумано число 3275 и названо число 1234,
# получаем в названном числе одного «быка» и одну «корову».
# Очевидно, что число отгадано в том случае, если имеем 4 «быка».

''')


def is_int(number):
    try:
        int(number)
        return True
    except ValueError:
        # print('Пиши число, а не свою фантазию')
        return False


def is_four_digit_number(number):
    if (number // 1000) > 0:
        return True
    else:
        # print('Число должно быть четырехзначным')
        return False


def is_number_has_different_numerals(number):
    numlist = []
    x = 1000
    for _ in range(4):
        num_i = ((number // (x * 10)) * 10) - (number // x)
        if num_i < 0:
            num_i = num_i * (-1)
        x = x // 10
        numlist.append(num_i)
    num_i = [0, 1, 2, 3]
    num_j = [1, 2, 3]
    for i in num_i:
        for j in num_j:
            if (numlist[i] == numlist[j]) and (i != j):
                return False
        if len(num_j) > 0:
            num_j.pop(0)
        if numlist[i] == numlist[j] and i != j:
            break
    if numlist[i] == numlist[j] and i != j:
        # print('Число должно иметь разные цифры')
        return False
    else:
        return True


def game(play_or_not):
    if play_or_not == 'Да':
        correct_number = mastermind_engine.get_number()
        cprint('Введи четырёхзначное число с разными цифрами', color='cyan')
        user_number = input()
        step = 1
        while True:
            while True:
                if is_int(user_number) == False:
                    cprint('Пиши число, а не свою фантазию', color='red')
                    print('')
                    user_number = input()
                    continue
                elif is_int(user_number) == True:
                    user_number = int(user_number)
                    if is_four_digit_number(user_number) == False:
                        cprint('Число должно быть четырехзначным', color='red')
                        print('')
                        user_number = input()
                        continue
                    elif is_four_digit_number(user_number) == True:
                        if is_number_has_different_numerals(user_number) == False:
                            cprint('Число должно иметь разные цифры', color='red')
                            print('')
                            user_number = input()
                            continue
                        elif is_number_has_different_numerals(user_number) == True:
                            break
            if mastermind_engine.check_number(number=user_number, true_number=correct_number)['bulls'] != 4:
                cprint('Быки - {}'.format(mastermind_engine.check_number(user_number, correct_number)['bulls']),
                       color='blue')
                cprint('Коровы - {}'.format(mastermind_engine.check_number(user_number, correct_number)['cows']),
                       color='blue')
                print('')
                cprint('Пробуй еще', color='cyan')
                user_number = input()
                step += 1
                continue
            else:
                break
        cprint('Ты выиграл, красава! Число угадано за {} шагов'.format(step), color='green')
        print('Хочешь еще партейку?) Введи Да/Нет')
        game(input())
        print('')
    if play_or_not == 'Нет':
        print('Жаль(((. Тогда сыграем в другой раз')
        os.system("pause")
    elif play_or_not != 'Да' and play_or_not != 'Нет':
        print('Не понял. Введи нормально!')
        game(input())
        print('')


game('Да')
