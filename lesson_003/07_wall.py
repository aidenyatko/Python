# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for
# TODO здесь ваш код
step = 0
for y in range(0, 5000, 50):
    for x in range(0, 10000, 150):
        if step == 0:
            point_list = [simple_draw.get_point(0 + x + step, 0 + y),
                          simple_draw.get_point(100 + x + step, 0 + y),
                          simple_draw.get_point(100 + x + step, 50 + y),
                          simple_draw.get_point(0 + x + step, 50 + y)]
            simple_draw.polygon(point_list=point_list)
            step += 50
        elif step == 50:
            point_list = [simple_draw.get_point(0 + x + step, 0 + y),
                          simple_draw.get_point(100 + x + step, 0 + y),
                          simple_draw.get_point(100 + x + step, 50 + y),
                          simple_draw.get_point(0 + x + step, 50 + y)]
            simple_draw.polygon(point_list=point_list)
            step = 0
simple_draw.pause()
