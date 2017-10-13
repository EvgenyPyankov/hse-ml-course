import pandas as pnd
import numpy as np
from utils import print_answer

data = pnd.read_csv('titanic.csv')


def get_percentage(x, count):
    return x / count * 100


def task1():
    # 1.Какое количество мужчин и женщин ехало на корабле? В качестве ответа
    # приведите два числа через пробел.

    sex_counts = data['Sex'].value_counts()
    line = str(sex_counts['male']) + ' ' + str(sex_counts['female'])
    print_answer(1, line)


def task2():
    # 2.Какой части пассажиров удалось выжить? Посчитайте долю выживших
    # пассажиров. Ответ приведите в процентах (число в интервале от 0 до 100,
    # знак процента не нужен), округлив до двух знаков.

    survived = data['Survived'].value_counts()
    srvd_prct = get_percentage(survived[1], survived.sum())
    print_answer(2, '{:0.2f}'.format(srvd_prct))


def task3():
    # 3.Какую долю пассажиры первого класса составляли среди всех пассажиров?
    # Ответ приведите в процентах (число в интервале от 0 до 100, знак процента
    # не нужен), округлив до двух знаков.

    pclass_counts = data['Pclass'].value_counts()
    first_pclass_prct = get_percentage(pclass_counts[1], pclass_counts.sum())
    print_answer(3, '{:0.2f}'.format(first_pclass_prct))


def task4():
    # 4.Какого возраста были пассажиры? Посчитайте среднее и медиану возраста
    # пассажиров. В качестве ответа приведите два числа через пробел.

    age = data['Age']
    line = '{:0.2f}'.format(age.mean()) + ' ' + '{:0.2f}'.format(age.median())
    print_answer(4, line)


def task5():
    # 5.Коррелируют ли число братьев/сестер/супругов с числом родителей/детей?
    # Посчитайте корреляцию Пирсона между признаками SibSp и Parch.

    print_answer(5, '{:0.2f}'.format(data['SibSp'].corr(data['Parch'])))


def task6():
    # 6.Какое самое популярное женское имя на корабле? Извлеките из полного
    # имени пассажира (колонка Name) его личное имя (First Name). Это задание —
    # типичный пример того, с чем сталкивается специалист по анализу данных.
    # Данные очень разнородные и шумные, но из них требуется извлечь необходимую
    # информацию. Попробуйте вручную разобрать несколько значений столбца Name и
    # выработать правило для извлечения имен, а также разделения их на женские и мужские.

    names = data['Name']
    names_array = np.array(names)
    for val in names_array:
        name = val.split()
        sex = name[1]
        if (sex == 'Mrs.' or sex == 'Miss.'):
            print(sex)

            # print(array[102].split())


task1()
task2()
task3()
task4()
task5()
task6()
