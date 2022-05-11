# -*- coding: utf-8 -*-

# (определение функций)
import simple_draw as sd

# Написать функцию отрисовки смайлика в произвольной точке экрана
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)


def smile(x, y, color):
    point = sd.get_point(x, y)
    sd.circle(center_position=point, radius=50, color=color)
    sd.line(start_point=sd.get_point(x - 20, y - 20), end_point=sd.get_point(x + 20, y - 20), color=color)
    sd.line(start_point=sd.get_point(x-27, y+20), end_point=sd.get_point(x-13, y+20), color=color)
    sd.line(start_point=sd.get_point(x+27, y+20), end_point=sd.get_point(x+13, y+20), color=color)


for _ in range(10):
    smile(sd.randint(60, 500), sd.randint(60, 500), color=sd.COLOR_RED)
sd.pause()
