# -*- coding: utf-8 -*-
from random import random, randint

import simple_draw as sd


# На основе вашего кода из решения lesson_004/01_shapes.py сделать функцию-фабрику,
# которая возвращает функции рисования треугольника, четырехугольника, пятиугольника и т.д.
#
# Функция рисования должна принимать параметры
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Функция-фабрика должна принимать параметр n - количество сторон.


def get_polygon(n):
    # Создание фиксированых точек
    equilateral_triangle_point = sd.get_point(100, 100)

    # Создание функции прямой
    v1 = sd.get_vector(equilateral_triangle_point, angle=0, length=0)

    def custom_line(start_point=v1.end_point, angle=0, length=100):
        v1 = sd.get_vector(start_point, angle=angle + 0, length=length)
        v1.draw()
        return v1.end_point

    # Создание функции фигур
    def equilateral_triangle(point, angle, length):
        custom_line(start_point=point, angle=angle, length=length)
        custom_line(start_point=custom_line(start_point=point, angle=angle, length=length), angle=angle - 120,
                    length=length)
        custom_line(start_point=custom_line(start_point=custom_line(start_point=point, angle=angle, length=length),
                                            angle=angle - 120, length=length), angle=angle + 120, length=length)
        return equilateral_triangle

    def square(point, angle, length):
        v1 = sd.get_vector(start_point=point, angle=angle + 0, length=length)
        v1.draw()
        v2 = sd.get_vector(start_point=point, angle=angle + 90, length=length)
        v2.draw()
        v3 = sd.get_vector(start_point=v1.end_point, angle=angle + 90, length=length)
        v3.draw()
        v4 = sd.get_vector(start_point=v2.end_point, angle=angle + 0, length=length)
        v4.draw()
        return square

    def equilateral_pentagon(point, angle, length):
        v1 = sd.get_vector(start_point=point, angle=angle + 0, length=length)
        v1.draw()
        v2 = sd.get_vector(start_point=point, angle=angle + 108, length=length)
        v2.draw()
        v3 = sd.get_vector(start_point=v1.end_point, angle=angle + 72, length=length)
        v3.draw()
        v4 = sd.get_vector(start_point=v2.end_point, angle=angle + 36, length=length)
        v4.draw()
        v5 = sd.get_vector(start_point=v4.end_point, angle=angle - 36, length=length)
        v5.draw()
        return equilateral_pentagon

    def equilateral_octagon(point, angle, length):
        v1 = sd.get_vector(start_point=point, angle=angle + 0, length=length)
        v1.draw()
        v2 = sd.get_vector(start_point=point, angle=angle + 120, length=length)
        v2.draw()
        v3 = sd.get_vector(start_point=v1.end_point, angle=angle + 60, length=length)
        v3.draw()
        v4 = sd.get_vector(start_point=v2.end_point, angle=angle + 60, length=length)
        v4.draw()
        v5 = sd.get_vector(start_point=v3.end_point, angle=angle + 120, length=length)
        v5.draw()
        v6 = sd.get_vector(start_point=v4.end_point, angle=angle + 0, length=length)
        v6.draw()
        return equilateral_octagon

    if n == 3:
        return equilateral_triangle
    elif n == 4:
        return square
    elif n == 5:
        return equilateral_pentagon
    elif n == 8:
        equilateral_octagon

    # TODO здесь ваш код


draw_triangle = get_polygon(n=8)
draw_triangle(point=sd.get_point(200, 200), angle=13, length=100)

sd.pause()
