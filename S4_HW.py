# =============================
# Methods. Здесь блок общих методов
from random import randint as rnd


def get_num(msg):
    while True:
        try:
            val = float(input(msg))
        except ValueError:
            print("Требуется число")
        else:
            return val


def get_rand_num(nonzero=False):
    while True:
        pass

# =============================

# A. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и
# записать в файл многочлен степени k.
# Пример:
# если k = 2, то многочлены могут быть => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0


def powch(num):
    if num < 2:
        return ''

    powchar_list = '⁰ ¹ ² ³ ⁴ ⁵ ⁶ ⁷ ⁸ ⁹ ⁺ ⁻ ⁼ ⁽ ⁾ ⁿ ⁱ'.split()

    if num < 10:
        return powchar_list[num]

    pw = ''
    while num >= 1:
        pw = powchar_list[int(num % 10)] + pw
        num /= 10
    return pw


def polynom_to_str(k, verbose=False):
    polynom_str = ''
    pw = k
    while pw >= 0:
        # koef = rnd(-100, 100)
        koef = rnd(-3, 3)
        # print(koef, end='    ')

        if pw == k:
            if not koef:
                continue

        if koef:
            if pw != k:
                polynom_str += ' + '
            if koef > 1 or koef < -1 or pw == 0:
                polynom_str += str(koef)
            elif koef == -1:
                polynom_str += '-'

            if pw:
                polynom_str += f"x{powch(pw)}" if not verbose else f"*x**{pw}"
        pw -= 1

    return polynom_str.replace(' + -', ' - ') + ' = 0'


# print('\n', polynom_to_str(14))

file_a = open('file_a', 'w')
file_b = open('file_b', 'w')

file_a.write(polynom_to_str(14, verbose=True))
file_b.write(polynom_to_str(14, verbose=True))

file_a.close()
file_b.close()

# B. Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.


def sum_two_polynom_str():
    pass


# sum_two_polynom_str()

# НЕОБЯЗАТЕЛЬНОЕ, ДОПОЛНИТЕЛЬНОЕ ЗАДАНИЕ:
# Расширить значение коэффициентов до [-100..100]
