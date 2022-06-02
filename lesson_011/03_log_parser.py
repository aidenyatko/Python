# -*- coding: utf-8 -*-

# На основе своего кода из lesson_009/02_log_parser.py напишите итератор (или генератор)
# который читает исходный файл events.txt и выдает число событий NOK за каждую минуту
# <время> <число повторений>
#
# пример использования:
#
# grouped_events = <создание итератора/генератора>
# for group_time, event_count in grouped_events:
#     print(f'[{group_time}] {event_count}')
#
# на консоли должно появится что-то вроде
#
# [2018-05-17 01:57] 1234

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
                        yield (prev_time + ']'), nok_count
                        nok_count = 1
                    prev_time = time
                    prev_line = line
            if (line.endswith('OK') or line.endswith('OK\n')) and \
                    (prev_line.endswith('NOK') or prev_line.endswith('NOK\n')):
                yield (prev_time + ']'), nok_count


grouped_events = LogStat('D:\courses\IT\Python\SkillBox_Python\Practice\lesson_009\events.txt')
for group_time, event_count in grouped_events.get_stat_by_time(min):
    print(f'[{group_time}] {event_count}')
