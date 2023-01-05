# =============================
# Methods. Здесь блок общих методов
from random import randint as rnd

file_a = 'file_a'
file_b = 'file_b'
file_sum = 'file_sum'
len_poly = 14

powchar_list = '⁰ ¹ ² ³ ⁴ ⁵ ⁶ ⁷ ⁸ ⁹ ⁺ ⁻ ⁼ ⁽ ⁾ ⁿ ⁱ'.split()

# =============================

# A. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и
# записать в файл многочлен степени k.
# Пример:
# если k = 2, то многочлены могут быть => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0


# Преобразует целые числа в (юникод) надстрочные
def num_to_powch(num):
    if num < 2:
        return ''

    if num < 10:
        return powchar_list[num]

    # pw = ''
    # while num >= 1:
    #     pw = powchar_list[int(num % 10)] + pw
    #     num /= 10

    # pw = [powchar_list[i] for i in str(num)]
    # return pw
    return ''.join([powchar_list[int(i)] for i in str(num)])


# Возвращает словарь коэффициентов для степеней до k
def rand_koefs(k):
    polynom_dict = {}
    pw = k
    while pw >= 0:
        koef = rnd(-100, 100)
        # koef = rnd(-3, 3)

        if pw == k:
            if not koef:
                continue

        polynom_dict[pw] = koef

        pw -= 1
    return polynom_dict


# принимает словарь, возвращает многочлен ввиде строки
def polynom_to_str(polydict: dict, verbose=False):
    polynom_str = ''
    for powr, koef in polydict.items():
        if koef:
            if powr != max(polydict.keys()):
                polynom_str += ' + '
            if koef > 1 or koef < -1 or powr == 0:
                polynom_str += str(koef)
            elif koef == -1:
                polynom_str += '-'

            if powr:
                polynom_str += f"x{num_to_powch(powr)}" if not verbose else f"*x**{powr}"

    return polynom_str.replace(' + -', ' - ') + ' = 0'


# print('\n', polynom_to_str(rand_koefs(len_poly)))


def str_to_files():
    fa = open(file_a, 'w')
    fb = open(file_b, 'w')

    fa.write(polynom_to_str(rand_koefs(len_poly)))
    fb.write(polynom_to_str(rand_koefs(len_poly)))

    fa.close()
    fb.close()

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
        rec = i.split('x')
        ky = powch_to_num(rec[1]) if len(rec) > 1 else 0
        vl = int(rec[0] if rec[0] and rec[0] != '-' else rec[0] + '1')
        poly_dict[ky] = vl

    # print('\n', poly_dict)
    return poly_dict


# Складывает (сумма) значения двух словарей
def sum_two_polynom(file_a, file_b):
    poly_a: dict = parse_poly(read_str_from_file(file_a))
    poly_b: dict = parse_poly(read_str_from_file(file_b))
    k = max(*poly_a.keys(), *poly_b.keys())

    poly_sum = {}

    for i in range(k, -1, -1):
        poly_sum[i] = poly_a.get(i, 0) + poly_b.get(i, 0)

    return poly_sum


str_to_files()
poly_str_sum = polynom_to_str(sum_two_polynom(file_a, file_b))


f = open(file_sum, 'w')
# print(poly_str_sum)
f.write(poly_str_sum)
f.close()

fa = open(file_a)
fb = open(file_b)
fsum = open(file_sum)

print(fa.readline())
print(fb.readline())
print(fsum.readline())

fa.close()
fb.close()
fsum.close()

# НЕОБЯЗАТЕЛЬНОЕ, ДОПОЛНИТЕЛЬНОЕ ЗАДАНИЕ:
# Расширить значение коэффициентов до [-100..100]
