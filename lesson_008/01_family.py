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

    def __init__(self, money_incidents, food_incidents):
        self.money = 100
        self.food = 50
        self.mess = 0
        self.cat_food = 30
        self.money_incidents = money_incidents
        self.food_incidents = food_incidents
        self.count_money_incidents = 0
        self.count_food_incidents = 0

    def __str__(self):
        return f'В доме {self.money} денег, {self.food} еды, {self.mess} грязи'

    def make_money_incidents(self):
        self.money = self.money // 2

    def make_food_incidents(self):
        self.food = self.food // 2

    def act(self):
        self.mess += 5
        dice_money = randint(1, 6)
        if self.count_money_incidents < self.money_incidents:
            if dice_money == 1:
                self.make_money_incidents()
                self.count_money_incidents += 1
        dice_food = randint(1, 6)
        if self.count_food_incidents < self.money_incidents:
            if dice_food == 1:
                self.make_food_incidents()
                self.count_food_incidents += 1


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
            # cprint(f'{self.name} поел(а)', color='blue')
            self.eaten_food = self.eaten_food + 30
        else:
            pass
            # cprint('В доме нет еды', color='yellow')

    def pet_the_cat(self):
        self.happiness += 5
        self.fullness -= 10
        # cprint(f'{self.name} погладил(а) кота', color='magenta')

    def act(self):
        if (self.fullness <= 0) or (self.happiness <= 0):
            # cprint(f'{self.name} умер', color='red')
            return
        if self.fullness <= 10 <= self.home.food:
            self.eat()

        if self.home.mess > 90:
            self.happiness -= 10


class Husband(Human):

    def __init__(self, name, home, salary):
        super().__init__(name=name, home=home)
        self.name = name
        self.home = home
        self.made_money = 0
        self.salary = salary

    def __str__(self):
        return super().__str__()

    def work(self):
        self.home.money += self.salary
        self.fullness -= 10
        # cprint(f'{self.name} поработал', color='green')
        self.made_money = self.made_money + self.salary

    def gaming(self):
        self.happiness += 20
        self.fullness -= 10
        # cprint(f'{self.name} поиграл в Assassin`s Creed', color='magenta')

    def act(self):
        if self.fullness > 10 and self.happiness > 0:
            dice = randint(1, 6)
            if self.home.money < (self.salary // 0.3):
                self.work()
            elif self.happiness <= 80:
                self.gaming()
            elif self.happiness <= 95:
                self.pet_the_cat()
        else:
            super(Husband, self).act()


class Wife(Human):

    def __init__(self, name, home, salary):
        super().__init__(name=name, home=home)
        self.name = name
        self.home = home
        self.fur_coat_bought = 0
        self.salary = salary

    def __str__(self):
        return super().__str__()

    def shopping(self):
        self.home.food += (self.salary // 0.7)
        self.home.money -= (self.salary // 0.7)
        self.fullness -= 10
        # cprint(f'{self.name} сходила за продуктами', color='green')

    def buy_fur_coat(self):
        self.home.money -= 350
        self.happiness += 60
        self.fullness -= 10
        # cprint(f'{self.name} купила шубу', color='yellow')
        self.fur_coat_bought += 1

    def clean_house(self, cleaning=80):
        self.home.mess -= cleaning
        self.fullness -= 10
        # cprint(f'{self.name} убирала дома', color='magenta')

    def buy_cat_food(self):
        self.home.cat_food += (self.salary // 3)
        self.home.money -= (self.salary // 3)
        self.fullness -= 10

    def act(self):
        if self.fullness >= 20 and self.happiness > 0:
            if self.home.mess >= 80:
                self.clean_house()
            elif self.home.food <= (self.salary // 0.7) <= self.home.money:
                self.shopping()
            elif self.home.cat_food <= (self.salary // 2):
                self.buy_cat_food()
            elif self.home.money >= 350 and self.happiness <= 40:
                self.buy_fur_coat()
            elif self.home.money < 350 and self.happiness <= 95:
                self.pet_the_cat()
            else:
                self.clean_house(5)
                # cprint(f'{self.name} ничего не делала')
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
            # cprint(f'{self.name} поел(а)', color='blue')
        else:
            pass
            # cprint('Нет кошачьей еды', color='yellow')

    def sleep(self):
        self.fullness -= 10
        # cprint(f'{self.name} поспал(а)', color='magenta')

    def soil(self):
        self.fullness -= 10
        self.home.mess += 5
        # cprint(f'{self.name} поцарапал(а) обои', color='yellow')

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
            # cprint(f'{self.name} поел(а)', color='blue')
        else:
            pass
            # cprint('Нет еды', color='yellow')

    def sleep(self):
        self.fullness -= 10
        # cprint(f'{self.name} поспал', color='magenta')

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
class Simulation:

    def __init__(self, money_incidents, food_incidents):
        self.money_incidents = money_incidents
        self.food_incidents = food_incidents

    def experiment(self, salary):
        home = House(money_incidents=self.money_incidents, food_incidents=self.food_incidents)
        dima = Husband(name='Дима', home=home, salary=salary)
        anya = Wife(name='Аня', home=home, salary=salary)
        danya = Child(name='Даня', home=home)
        cats = [Cat(name='Мася', home=home), Cat(name='Леопольд', home=home), Cat(name='Гарфилд', home=home),
                Cat(name='Бегемот', home=home), Cat(name='Чешир', home=home), Cat(name='Кот-Ученый', home=home),
                Cat(name='Кот в Сапогах', home=home), Cat(name='Персик', home=home), Cat(name='Киберкот', home=home),
                Cat(name='Вася', home=home), Cat(name='Снежок', home=home), Cat(name='Дыбил', home=home),
                Cat(name='Идиот', home=home), Cat(name='Триод', home=home), Cat(name='Гамнюк', home=home),
                Cat(name='Пятныш', home=home), Cat(name='Шерсть', home=home), Cat(name='Рыжик', home=home)]
        for num_of_cats in range(len(cats)):
            for day in range(1, 366):
                # cprint('================== День {} =================='.format(day), color='red')
                dima.act()
                anya.act()
                danya.act()
                for current_num_of_cats in range(num_of_cats + 1):
                    cats[current_num_of_cats].act()
                home.act()
                # cprint(dima, color='cyan')
                # cprint(anya, color='cyan')
                # for current_num_of_cats in range(num_of_cats + 1):
                #     cprint(cats[current_num_of_cats], color='cyan')
                # cprint(home, color='cyan')
                # cprint(danya, color='cyan')
                if (dima.fullness <= 0 or dima.happiness <= 0) or (anya.fullness <= 0 or anya.happiness <= 0):
                    if num_of_cats > 0:
                        return num_of_cats - 1
                    else:
                        return num_of_cats
                for cat in range(current_num_of_cats + 1):
                    if cats[cat].fullness <= 0:
                        if num_of_cats > 0:
                            return num_of_cats - 1
                        else:
                            return num_of_cats
                    elif cat >= 12:
                        return 12
        # cprint('=======================Итог за год==================', color='white')
        total_eaten_food = dima.eaten_food + anya.eaten_food + danya.eaten_food
        total_made_money = dima.made_money
        total_fur_coat_bought = anya.fur_coat_bought
        # cprint(
        # f'{total_eaten_food} еды съедено, {total_made_money} денег заработано, {total_fur_coat_bought} шуб куплено')


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
count = 0
for food_incidents in range(6):
    for money_incidents in range(6):
        life = Simulation(money_incidents, food_incidents)
        count += 1
        print(f"({count})")
        for salary in range(50, 401, 50):
            max_cats = life.experiment(salary)
            print(f'При зарплате {salary} максимально можно прокормить {max_cats} котов')
        print('')
# life = Simulation(0, 0)
# for salary in range(50, 401, 50):
#     max_cat = life.experiment(salary)
#     print(f'''{max_cat}''')
