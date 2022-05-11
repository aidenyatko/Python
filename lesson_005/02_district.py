# -*- coding: utf-8 -*-

# Составить список всех живущих на районе и Вывести на консоль через запятую
# Формат вывода: На районе живут ...
# подсказка: для вывода элементов списка через запятую можно использовать функцию строки .join()
# https://docs.python.org/3/library/stdtypes.html#str.join

# TODO здесь ваш код

import district.central_street.house1.room1 as dch1r1
import district.central_street.house1.room2 as dch1r2
import district.central_street.house2.room1 as dch2r1
import district.central_street.house2.room2 as dch2r2
import district.soviet_street.house1.room1 as dsh1r1
import district.soviet_street.house1.room2 as dsh1r2
import district.soviet_street.house2.room1 as dsh2r1
import district.soviet_street.house2.room2 as dsh2r2

# import district
# q = district.central_street.house1.room1.folks
# pprint(q)

rooms = dch1r1.folks, dch1r2.folks, dch2r1.folks, dch2r2.folks, dsh1r1.folks, dsh1r2.folks, dsh2r1.folks, \
        dsh2r2.folks

people = []
for _ in rooms:
    people = people + _

print(','.join(people))
