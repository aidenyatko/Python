# -*- coding: utf-8 -*-

from random import randint

from termcolor import cprint


######################################################## Часть первая
#
# Создать модель жизни небольшой семьи.
#
# Каждый день участники жизни могут делать только одно действие.
# Все вместе они должны прожить год и не умереть.
#
# Муж может:
#   есть,
#   играть в WoT,
#   ходить на работу,
# Жена может:
#   есть,
#   покупать продукты,
#   покупать шубу,
#   убираться в доме,

# Все они живут в одном доме, дом характеризуется:
#   кол-во денег в тумбочке (в начале - 100)
#   кол-во еды в холодильнике (в начале - 50)
#   кол-во грязи (в начале - 0)
#
# У людей есть имя, степень сытости (в начале - 30) и степень счастья (в начале - 100).
#
# Любое действие, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Кушают взрослые максимум по 30 единиц еды, степень сытости растет на 1 пункт за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе чел умрет от голода.
#
# Деньги в тумбочку добавляет муж, после работы - 150 единиц за раз.
# Еда стоит 10 денег 10 единиц еды. Шуба стоит 350 единиц.
#
# Грязь добавляется каждый день по 5 пунктов, за одну уборку жена может убирать до 100 единиц грязи.
# Если в доме грязи больше 90 - у людей падает степень счастья каждый день на 10 пунктов,
# Степень счастья растет: у мужа от игры в WoT (на 20), у жены от покупки шубы (на 60, но шуба дорогая)
# Степень счастья не должна падать ниже 10, иначе чел умирает от депрессии.
#
# Подвести итоги жизни за год: сколько было заработано денег, сколько съедено еды, сколько куплено шуб.

class House:

    def __init__(self):
        self.money = 100
        self.food = 50
        self.mess = 0
        self.cat_food = 30

    def __str__(self):
        return f'В доме {self.money} денег, {self.food} еды, {self.mess} грязи'

    def act(self):
        self.mess += 5


class Human:
    def __init__(self, name, home):
        self.name = name
        self.fullness = 30
        self.happiness = 100
        self.home = home
        self.eaten_food = 0

    def __str__(self):
        return f'Я {self.name}. Моя сытость равна {self.fullness}. А счастлив(а) я на все {self.happiness}'

    def eat(self):
        if self.home.food >= 30:
            self.fullness += 30
            self.home.food -= 30
            cprint(f'{self.name} поел(а)', color='blue')
            self.eaten_food = self.eaten_food + 30
        else:
            cprint('В доме нет еды', color='yellow')

    def pet_the_cat(self):
        self.happiness += 5
        self.fullness -= 10
        cprint(f'{self.name} погладил(а) кота', color='magenta')

    def act(self):
        if (self.fullness <= 0) or (self.happiness <= 0):
            cprint(f'{self.name} умер', color='red')
            return
        if self.fullness <= 10 <= self.home.food:
            self.eat()

        if self.home.mess > 90:
            self.happiness -= 10


class Husband(Human):

    def __init__(self, name, home):
        super().__init__(name=name, home=home)
        self.name = name
        self.home = home
        self.made_money = 0

    def __str__(self):
        return super().__str__()

    def work(self):
        self.home.money += 150
        self.fullness -= 10
        cprint(f'{self.name} поработал', color='green')
        self.made_money = self.made_money + 150

    def gaming(self):
        self.happiness += 20
        self.fullness -= 10
        cprint(f'{self.name} поиграл в Assassin`s Creed', color='magenta')

    def act(self):
        if self.fullness > 10 and self.happiness > 0:
            dice = randint(1, 6)
            if self.home.money < 770 or dice in [3, 4]:
                self.work()
            elif dice in [1, 2]:
                self.gaming()
            else:
                self.pet_the_cat()
        else:
            super(Husband, self).act()


class Wife(Human):

    def __init__(self, name, home):
        super().__init__(name=name, home=home)
        self.name = name
        self.home = home
        self.fur_coat_bought = 0

    def __str__(self):
        return super().__str__()

    def shopping(self):
        self.home.food += 210
        self.home.money -= 210
        self.fullness -= 10
        cprint(f'{self.name} сходила за продуктами', color='green')

    def buy_fur_coat(self):
        self.home.money -= 350
        self.happiness += 60
        self.fullness -= 10
        cprint(f'{self.name} купила шубу', color='yellow')
        self.fur_coat_bought += 1

    def clean_house(self):
        self.home.mess -= 80
        self.fullness -= 10
        cprint(f'{self.name} убирала дома', color='magenta')

    def buy_cat_food(self):
        self.home.cat_food += 35
        self.home.money -= 35
        self.fullness -= 10

    def act(self):
        if self.fullness >= 20 and self.happiness > 0:
            if self.home.mess >= 80:
                self.clean_house()
            elif self.home.food <= 210 <= self.home.money:
                self.shopping()
            elif self.home.cat_food <= 35:
                self.buy_cat_food()
            elif self.home.money >= 350:
                dice = randint(1, 4)
                if dice == 1:
                    self.buy_fur_coat()
                else:
                    self.pet_the_cat()
            elif self.home.money < 350:
                self.pet_the_cat()
            else:
                cprint(f'{self.name} ничего не делала')
        else:
            super(Wife, self).act()


# home = House()
# serge = Husband(name='Сережа', home=home)
# masha = Wife(name='Маша', home=home)
#
# for day in range(1, 366):
#     cprint('================== День {} =================='.format(day), color='red')
#     serge.act()
#     masha.act()
#     home.act()
#     cprint(serge, color='cyan')
#     cprint(masha, color='cyan')
#     cprint(home, color='cyan')
#
# cprint('=======================Итог за год==================', color='white')
# total_eaten_food = serge.eaten_food + masha.eaten_food
# total_made_money = serge.made_money
# total_fur_coat_bought = masha.fur_coat_bought
# cprint(f'{total_eaten_food} еды съедено, {total_made_money} денег заработано, {total_fur_coat_bought} шуб куплено')


# TODO после реализации первой части - отдать на проверку учителю

######################################################## Часть вторая
#
# После подтверждения учителем первой части надо
# отщепить ветку develop и в ней начать добавлять котов в модель семьи
#
# Кот может:
#   есть,
#   спать,
#   драть обои
#
# Люди могут:
#   гладить кота (растет степень счастья на 5 пунктов)
#
# В доме добавляется:
#   еда для кота (в начале - 30)
#
# У кота есть имя и степень сытости (в начале - 30)
# Любое действие кота, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Еда для кота покупается за деньги: за 10 денег 10 еды.
# Кушает кот максимум по 10 единиц еды, степень сытости растет на 2 пункта за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе кот умрет от голода.
#
# Если кот дерет обои, то грязи становится больше на 5 пунктов


class Cat:

    def __init__(self, name, home):
        self.name = name
        self.fullness = 0
        self.home = home

    def __str__(self):
        return f'Я {self.name}, моя сытость {self.fullness}'

    def eat(self):
        if self.home.cat_food >= 10:
            self.fullness += 10
            self.home.cat_food -= 10
            cprint(f'{self.name} поел(а)', color='blue')
        else:
            cprint('Нет кошачьей еды', color='yellow')

    def sleep(self):
        self.fullness -= 10
        cprint(f'{self.name} поспал(а)', color='magenta')

    def soil(self):
        self.fullness -= 10
        self.home.mess += 5
        cprint(f'{self.name} поцарапал(а) обои', color='yellow')

    def act(self):
        if self.fullness <= 20:
            self.eat()
        else:
            dice = randint(1, 6)
            if dice in range(1, 4):
                self.soil()
            else:
                self.sleep()


######################################################## Часть вторая бис
#
# После реализации первой части надо в ветке мастер продолжить работу над семьей - добавить ребенка
#
# Ребенок может:
#   есть,
#   спать,
#
# отличия от взрослых - кушает максимум 10 единиц еды,
# степень счастья - не меняется, всегда ==100 ;)

class Child(Human):

    def __init__(self, name, home):
        super().__init__(name=name, home=home)
        self.name = name
        self.home = home
        self.happiness = 100

    def __str__(self):
        return super().__str__()

    def eat(self):
        if self.home.food >= 10:
            self.fullness += 10
            cprint(f'{self.name} поел(а)', color='blue')
        else:
            cprint('Нет еды', color='yellow')

    def sleep(self):
        self.fullness -= 10
        cprint(f'{self.name} поспал', color='magenta')

    def act(self):
        if self.fullness <= 35:
            self.eat()
        else:
            self.sleep()


# TODO после реализации второй части - отдать на проверку учителем две ветки


######################################################## Часть третья
#
# после подтверждения учителем второй части (обоих веток)
# влить в мастер все коммиты из ветки develop и разрешить все конфликты
# отправить на проверку учителем.


home = House()
dima = Husband(name='Дима', home=home)
anya = Wife(name='Аня', home=home)
masya = Cat(name='Мася', home=home)
danya = Child(name='Даня', home=home)

for day in range(1, 366):
    cprint('================== День {} =================='.format(day), color='red')
    dima.act()
    anya.act()
    danya.act()
    masya.act()
    home.act()
    cprint(dima, color='cyan')
    cprint(anya, color='cyan')
    cprint(masya, color='cyan')
    cprint(home, color='cyan')
    cprint(danya, color='cyan')

cprint('=======================Итог за год==================', color='white')
total_eaten_food = dima.eaten_food + anya.eaten_food + danya.eaten_food
total_made_money = dima.made_money
total_fur_coat_bought = anya.fur_coat_bought
cprint(f'{total_eaten_food} еды съедено, {total_made_money} денег заработано, {total_fur_coat_bought} шуб куплено')

# Усложненное задание (делать по желанию)
#
# Сделать из семьи любителей котов - пусть котов будет 3, или даже 5-10.
# Коты должны выжить вместе с семьей!
#
# Определить максимальное число котов, которое может прокормить эта семья при значениях зарплаты от 50 до 400.
# Для сглаживание случайностей моделирование за год делать 3 раза, если 2 из 3х выжили - считаем что выжили.
#
# Дополнительно вносить некий хаос в жизнь семьи
# - N раз в год вдруг пропадает половина еды из холодильника (коты?)
# - K раз в год пропадает половина денег из тумбочки (муж? жена? коты?!?!)
# Промоделировать - как часто могут случаться фейлы что бы это не повлияло на жизнь героев?
#   (N от 1 до 5, K от 1 до 5 - нужно вычислит максимумы N и K при котором семья гарантированно выживает)
#
# в итоге должен получится приблизительно такой код экспериментов
# for food_incidents in range(6):
#   for money_incidents in range(6):
#       life = Simulation(money_incidents, food_incidents)
#       for salary in range(50, 401, 50):
#           max_cats = life.experiment(salary)
#           print(f'При зарплате {salary} максимально можно прокормить {max_cats} котов')
