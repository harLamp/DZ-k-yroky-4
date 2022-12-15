"""Реализовать скрипт, в котором должна быть предусмотрена функция расчета
заработной платы сотрудника. В расчете необходимо использовать формулу:
(выработка в часах*ставка в час) + премия. Для выполнения расчета для
конкретных значений необходимо запускать скрипт с параметрами."""

# 1 Вводим нам необходимые нам параметры
def sal(hours, rate, bonus):
    try:
        res = (working_hours * working_rate) + (bonus * working_hours)
        print(f'Сотрудник {name_worker} заработал {res}')
    except TypeError:
        print(f'Error')
        exit()
name_worker = input('Имя сотрудника ')
working_hours = float(input('Выработка в часах '))
working_rate = int(input('Ставка '))
bonus = int(input('Премия '))
sal(working_hours, working_rate, bonus)


# 2 Задаем параметры в Edit Configurations

from sys import argv

name_script, name_worker, working_hours, working_rate, bonus = argv

try:
    name_worker = str(name_worker)
    working_hours = int(working_hours)
    working_rate = int(working_rate)
    bonus = int(bonus)
    res = (working_hours * working_rate) + (bonus * working_hours)
    print(f'Сотрудник {name_worker} заработал {res}')
except ValueError:
    print('Not a number')