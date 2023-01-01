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


def polynom_to_str(k):
    polynom_str = ''
    for i in range(k, -1, -1):
        if i == k:
            while True:
                koef = rnd(-100, 100)
                if koef:
                    polynom_str = f"{koef}x{powch(i)}"
                    break
        # elif i:
        else:
            koef = rnd(-100, 100)
            polynom_str += f" + {koef}x{powch(i)}"

    return polynom_str.replace(' + -', ' - ') + ' = 0'

print(polynom_to_str(14))


# B. Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.


def sum_two_polynom_str():
    pass


# sum_two_polynom_str()

# НЕОБЯЗАТЕЛЬНОЕ, ДОПОЛНИТЕЛЬНОЕ ЗАДАНИЕ:
# Расширить значение коэффициентов до [-100..100]
