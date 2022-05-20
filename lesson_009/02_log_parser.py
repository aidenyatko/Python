# -*- coding: utf-8 -*-

# Имеется файл events.txt вида:
#
# [2018-05-17 01:55:52.665804] NOK
# [2018-05-17 01:56:23.665804] OK
# [2018-05-17 01:56:55.665804] OK
# [2018-05-17 01:57:16.665804] NOK
# [2018-05-17 01:57:58.665804] OK
# ...
#
# Напишите программу, которая считывает файл
# и выводит число событий NOK за каждую минуту в другой файл в формате
#
# [2018-05-17 01:57] 1234
# [2018-05-17 01:58] 4321
# ...
#
# Входные параметры: файл для анализа, файл результата
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.

# TODO здесь ваш код
class LogStat:

    def __init__(self, logfile):
        self.logfile = logfile

    def get_stat_by_time(self, way):
        with open(self.logfile, 'r') as log:
            if way == 'min':
                sort = 17
            elif way == 'hour':
                sort = 14
            elif way == 'month':
                sort = 8
            elif way == 'year':
                sort = 5
            nok_count = 1
            prev_time = None
            for line in log:
                time = line[:sort]
                if line.endswith('NOK') or line.endswith('NOK\n'):
                    if prev_time == time and prev_time is not None:
                        nok_count += 1
                    elif prev_time is not None:
                        print(prev_time + ']' + ' ' + str(nok_count))
                        nok_count = 1
                    prev_time = time
                    prev_line = line
            if (line.endswith('OK') or line.endswith('OK\n')) and \
                    (prev_line.endswith('NOK') or prev_line.endswith('NOK\n')):
                print(prev_time + ']' + ' ' + str(nok_count))


log_stat = LogStat('events.txt')
log_stat.get_stat_by_time(way='year')
# После выполнения первого этапа нужно сделать группировку событий
#  - по часам
#  - по месяцу
#  - по году
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
