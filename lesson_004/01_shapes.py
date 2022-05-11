# -*- coding: utf-8 -*-
import random

import simple_draw as sd

# Часть 1.
# Написать функции рисования равносторонних геометрических фигур:
# - треугольника
# - квадрата
# - пятиугольника
# - шестиугольника
# Все функции должны принимать 3 параметра:
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Использование копи-пасты - обязательно! Даже тем кто уже знает про её пагубность. Для тренировки.
# Как работает копипаста:
#   - одну функцию написали,
#   - копипастим её, меняем название, чуть подправляем код,
#   - копипастим её, меняем название, чуть подправляем код,
#   - и так далее.
# В итоге должен получиться ПОЧТИ одинаковый код в каждой функции

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# sd.line()
# Результат решения см lesson_004/results/exercise_01_shapes.jpg

# TODO здесь ваш код
# Создание точек
# Создание фиксированых точек
equilateral_triangle_point = sd.get_point(100, 100)
square_point = sd.get_point(100, 400)
equilateral_pentagon_point = sd.get_point(400, 100)
equilateral_octagon_point = sd.get_point(400, 400)

# Создание рандомных точек
random_point_equilateral_triangle = sd.random_point()
random_point_square = sd.random_point()
random_point_equilateral_pentagon = sd.random_point()
random_point_octagon = sd.random_point()

# Создание рандомного угла
random_angle = random.uniform(0, 360)


# Создание функции прямой
v1 = sd.get_vector(equilateral_triangle_point, angle=0, length=0)


def custom_line(start_point=v1.end_point, angle=0, length=100):
    v1 = sd.get_vector(start_point, angle=angle + 0, length=length)
    v1.draw()


# Создание функции фигур
def equilateral_triangle(start_point, angle, length):
    for _ in range(3):
        custom_line(start_point=start_point, angle=angle, length=length)
        start_point = v1.end_point



def square(start_point, angle, length):
    v1 = sd.get_vector(start_point=start_point, angle=angle + 0, length=length)
    v1.draw()
    v2 = sd.get_vector(start_point=start_point, angle=angle + 90, length=length)
    v2.draw()
    v3 = sd.get_vector(start_point=v1.end_point, angle=angle + 90, length=length)
    v3.draw()
    v4 = sd.get_vector(start_point=v2.end_point, angle=angle + 0, length=length)
    v4.draw()


def equilateral_pentagon(start_point, angle, length):
    v1 = sd.get_vector(start_point=start_point, angle=angle + 0, length=length)
    v1.draw()
    v2 = sd.get_vector(start_point=start_point, angle=angle + 108, length=length)
    v2.draw()
    v3 = sd.get_vector(start_point=v1.end_point, angle=angle + 72, length=length)
    v3.draw()
    v4 = sd.get_vector(start_point=v2.end_point, angle=angle + 36, length=length)
    v4.draw()
    v5 = sd.get_vector(start_point=v4.end_point, angle=angle - 36, length=length)
    v5.draw()


def equilateral_octagon(start_point, angle, length):
    v1 = sd.get_vector(start_point=start_point, angle=angle + 0, length=length)
    v1.draw()
    v2 = sd.get_vector(start_point=start_point, angle=angle + 120, length=length)
    v2.draw()
    v3 = sd.get_vector(start_point=v1.end_point, angle=angle + 60, length=length)
    v3.draw()
    v4 = sd.get_vector(start_point=v2.end_point, angle=angle + 60, length=length)
    v4.draw()
    v5 = sd.get_vector(start_point=v3.end_point, angle=angle + 120, length=length)
    v5.draw()
    v6 = sd.get_vector(start_point=v4.end_point, angle=angle + 0, length=length)
    v6.draw()


# Вызов функций фигур
equilateral_triangle(start_point=equilateral_triangle_point, angle=0, length=100)
# square(start_point=square_point, angle=0, length=50)
# equilateral_pentagon(start_point=equilateral_pentagon_point, angle=0, length=50)
# equilateral_octagon(start_point=equilateral_octagon_point, angle=0, length=50)
# custom_line(equilateral_triangle_point, 0, 100)

# Часть 1-бис.
# Попробуйте прикинуть обьем работы, если нужно будет внести изменения в этот код.
# Скажем, связывать точки не линиями, а дугами. Или двойными линиями. Или рисовать круги в угловых точках. Или...
# А если таких функций не 4, а 44?

# Часть 2 (делается после зачета первой части)
#
# Надо сформировать функцию, параметризированную в местах где была "небольшая правка".
# Это называется "Выделить общую часть алгоритма в отдельную функцию"
# Потом надо изменить функции рисования конкретных фигур - вызывать общую функцию вместо "почти" одинакового кода.
#
# В итоге должно получиться:
#   - одна общая функция со множеством параметров,
#   - все функции отрисовки треугольника/квадрата/етс берут 3 параметра и внутри себя ВЫЗЫВАЮТ общую функцию.
#
# Не забудте в этой общей функции придумать, как устранить разрыв
#   в начальной/конечной точках рисуемой фигуры (если он есть)

# Часть 2-бис.
# А теперь - сколько надо работы что бы внести изменения в код? Выгода на лицо :)
# Поэтому среди программистов есть принцип D.R.Y. https://clck.ru/GEsA9
# Будьте ленивыми, не используйте копи-пасту!


sd.pause()
