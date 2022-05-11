# -*- coding: utf-8 -*-

# (цикл while)

# Ежемесячная стипендия студента составляет educational_grant руб., а расходы на проживание превышают стипендию
# и составляют expenses руб. в месяц. Рост цен ежемесячно увеличивает расходы на 3%, кроме первого месяца
# Составьте программу расчета суммы денег, которую необходимо единовременно попросить у родителей,
# чтобы можно было прожить учебный год (10 месяцев), используя только эти деньги и стипендию.
# Формат вывода:
#   Студенту надо попросить ХХХ.ХХ рублей

# educational_grant, expenses = 10000, 12000


def money():
    user_input = input('Введите сумму стипендии ')
    educational_grant = int(user_input)
    user_input = input('Введите сумму затрат ')
    expenses = int(user_input)
    user_input = input('Введите кол-во месяцев ')
    last_month = int(user_input)
    mounth = 1
    while mounth <= last_month:
        if mounth == 1:
            difference = expenses - educational_grant
        elif mounth > 1:
            expenses += expenses * 0.03
            difference = difference + expenses - educational_grant
        mounth += 1
    return difference


money()
print('Всего мне надо бы', round(money(), 2))
