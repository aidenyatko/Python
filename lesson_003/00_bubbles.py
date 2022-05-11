# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 600)

COLOR_WHITE = (255, 255, 255)
COLOR_BLACK = (0, 0, 0)

COLOR_RED = (255, 0, 0)
COLOR_ORANGE = (255, 127, 0)
COLOR_YELLOW = (255, 255, 0)
COLOR_GREEN = (0, 255, 0)
COLOR_CYAN = (0, 255, 255)
COLOR_BLUE = (0, 0, 255)
COLOR_PURPLE = (255, 0, 255)

COLOR_DARK_YELLOW = (127, 127, 0)
COLOR_DARK_ORANGE = (127, 63, 0)
COLOR_DARK_RED = (127, 0, 0)
COLOR_DARK_GREEN = (0, 127, 0)
COLOR_DARK_CYAN = (0, 127, 127)
COLOR_DARK_BLUE = (0, 0, 127)
COLOR_DARK_PURPLE = (127, 0, 127)


# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей
# for step_radius in range(50, 160, 50):
#     point = sd.get_point(200, 200)
#     radius = step_radius
#     sd.circle(point, step_radius)
# Написать функцию рисования пузырька, принммающую 2 (или более) параметра: точка рисовании и шаг
# TODO здесь ваш код
def buble(point, step=3, color=(255, 0, 0)):
    radius = 25
    for _ in range(3):
        radius += step
        # color = color
        sd.circle(center_position=point, radius=radius, color=color)


# point = sd.get_point(100, 100)
# buble(point=point, step=100)
# Нарисовать 10 пузырьков в ряд
# for x in range(75, 751, 75):
#     point = sd.get_point(x, 100)
#     buble(point=point, step=5)
# Нарисовать три ряда по 10 пузырьков
# for x in range(75, 751, 75):
#     for y in range(75, 751, 75):
#         point = sd.get_point(x, y)
#         buble(point=point, step=5)
# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
for _ in range(1000):
    point = sd.random_point()
    color = sd.random_color()
    buble(point, color=color)
sd.pause()
