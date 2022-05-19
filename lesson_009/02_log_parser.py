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

    def get_stat_by_min(self):
        with open(self.logfile, 'r') as log:
            nok_count = 1
            prev_time = None
            prev_line = None
            for line in log:
                time = line[12:17]
                if line.endswith('NOK\n') or line.endswith('NOK'):
                    if prev_time == time:
                        nok_count += 1
                        continue
                    else:
                        nok_count = 1
                        prev_time = time
                    if prev_line is None:
                        prev_line = line
                    stat = prev_line[:17] + '] ' + str(nok_count)
                    if prev_time is not None:
                        print(stat)
                    prev_line = line


log_stat = LogStat('events.txt')
log_stat.get_stat_by_min()
# После выполнения первого этапа нужно сделать группировку событий
#  - по часам
#  - по месяцу
#  - по году
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
