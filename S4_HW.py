# =============================
# Methods. Здесь блок общих методов
from random import randint as rnd

file_a = 'file_a'
file_b = 'file_b'
file_sum = 'file_sum'
len_poly = 14

powchar_list = '⁰ ¹ ² ³ ⁴ ⁵ ⁶ ⁷ ⁸ ⁹ ⁺ ⁻ ⁼ ⁽ ⁾ ⁿ ⁱ'.split()


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


# Преобразует целые числа в (юникод) надстрочные
def powch(num):
    if num < 2:
        return ''

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
        koef = rnd(-100, 100)
        # koef = rnd(-3, 3)
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


# print('\n', polynom_to_str(len_poly))

def str_to_files():
    file_a = open(file_a, 'w')
    file_b = open(file_b, 'w')

    file_a.write(polynom_to_str(14))
    file_b.write(polynom_to_str(14))

    file_a.close()
    file_b.close()


# str_to_files()

# B. Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

# Возвращает первую строку файла
def read_str_from_file(file_):
    f = open(file_)
    _string = f.readline()
    f.close()
    return _string


# Преобразует (юникод) надстрочные числа в целые
def powch_to_num(powch_):
    if powch_ == '':
        return 1

    num = ''
    for i in powch_:
        num += str(powchar_list.index(i))
    return int(num)


# Разбирает строку на члены, возвращает словарь
def parse_poly(_string: str):
    poly_dict = {}
    poly_arr = _string.replace(' ', '').replace(
        '-', ' -').replace('+', ' ').replace('=0', '').lower().split()

    for i in poly_arr:
        print(i, end=' ')
        rec = i.split('x')
        ky = powch_to_num(rec[1]) if len(rec) > 1 else 0
        poly_dict[ky] = int(rec[0])

    print('\n', poly_dict)
    return poly_dict


# Складывает (сумма) значения двух словарей
def sum_two_polynom(k):
    poly_a: dict = parse_poly(read_str_from_file(file_a))
    poly_b: dict = parse_poly(read_str_from_file(file_b))
    poly_sum = {}

    for i in range(k+1):
        poly_sum[i] = poly_a.get(i, 0) + poly_b.get(i, 0)

    return poly_sum


print(sum_two_polynom(len_poly))

# НЕОБЯЗАТЕЛЬНОЕ, ДОПОЛНИТЕЛЬНОЕ ЗАДАНИЕ:
# Расширить значение коэффициентов до [-100..100]
