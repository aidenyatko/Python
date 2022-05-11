# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)


# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)
def rainbow_line():
    step = 0
    for color in rainbow_colors:
        sd.line(start_point=sd.get_point(50 + step, 50), end_point=sd.get_point(350 + step, 450), color=color, width=4)
        step += 5


# rainbow_line()

# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво
# TODO здесь ваш код
def rainbow():
    step = 0
    for color in rainbow_colors:
        sd.circle(center_position=sd.get_point(300, 0), radius=300+step, color=color, width=10)
        step += 5


# rainbow()

sd.pause()
