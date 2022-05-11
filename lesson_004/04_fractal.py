# -*- coding: utf-8 -*-

import simple_draw as sd


# 1) Написать функцию draw_branches, которая должна рисовать две ветви дерева из начальной точки
# Функция должна принимать параметры:
# - точка начала рисования,
# - угол рисования,
# - длина ветвей,
# Отклонение ветвей от угла рисования принять 30 градусов,

# 2) Сделать draw_branches рекурсивной
# - добавить проверку на длину ветвей, если длина меньше 10 - не рисовать
# - вызывать саму себя 2 раза из точек-концов нарисованных ветвей,
#   с параметром "угол рисования" равным углу только что нарисованной ветви,
#   и параметром "длинна ветвей" в 0.75 меньшей чем длина только что нарисованной ветви

# 3) первоначальный вызов:
# root_point = get_point(300, 30)
# draw_bunches(start_point=root_point, angle=90, length=100)

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# Возможный результат решения см lesson_004/results/exercise_04_fractal_01.jpg

# можно поиграть -шрифтами- цветами и углами отклонения

# TODO здесь ваш код
def draw_branches(start_point=sd.get_point(300, 0), angle=90, length=300):
    if length < 10:
        return
    v1 = sd.get_vector(start_point=start_point, angle=angle+30, length=length, width=1)
    v2 = sd.get_vector(start_point=start_point, angle=angle - 30, length=length, width=1)
    v3 = sd.get_vector(start_point=start_point, angle=angle + 60, length=length, width=1)
    v4 = sd.get_vector(start_point=start_point, angle=angle - 60, length=length, width=1)
    v5 = sd.get_vector(start_point=start_point, angle=angle, length=length, width=1)
    v1.draw()
    v2.draw()
    v3.draw()
    v4.draw()
    v5.draw()
    draw_branches(start_point=v1.end_point, length=length*0.75, angle=angle+10)
    draw_branches(start_point=v2.end_point, length=length*0.75, angle=angle-10)
    draw_branches(start_point=v3.end_point, length=length * 0.75, angle=angle + 10)
    draw_branches(start_point=v4.end_point, length=length * 0.75, angle=angle-10)
    draw_branches(start_point=v5.end_point, length=length * 0.75, angle=angle)


draw_branches()
# 4) Усложненное задание (делать по желанию)
# - сделать рандомное отклонение угла ветвей в пределах 40% от 30-ти градусов
# - сделать рандомное отклонение длины ветвей в пределах 20% от коэффициента 0.75
# Возможный результат решения см lesson_004/results/exercise_04_fractal_02.jpg

# Пригодятся функции
# sd.random_number()

sd.pause()
