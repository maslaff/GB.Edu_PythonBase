# =============================
# Methods. Здесь блок общих методов
import time


def get_num(msg):
    while True:
        try:
            val = float(input(msg))
        except ValueError:
            print("Требуется число")
        else:
            return val

# =============================

# Напишите программу, которая принимает на вход вещественное число и
# показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11


def sum_dig_of_float():
    # in_num = input("Введите число: ") # Так можно вводить вещественное число с запятой как в примере
    # Так только с точкой, но зато с проверкой ввода
    in_num = str(get_num("Введите число: "))
    acc = 0
    for i in in_num:
        if i in [',', '.']:
            continue
        acc += int(i)
    print(acc)


# sum_dig_of_float()


# Задайте список из n чисел последовательности (1 + 1/n)**n,
# выведеите его на экран, а так же сумму элементов списка.
# Пример:
# Для n=4 -> [2, 2.25, 2.37, 2.44]
# Сумма 9.06


def list_serial_num():
    num_list = []
    acc = 0
    n = int(get_num("Введите число: "))
    for i in range(1, n+1):
        val = (1+1/i)**i
        num_list.append(round(val, 2) if val % 1 else int(val))
        acc += val
    print(f"Для n={n} -> {num_list}\nСумма {round(acc, 2)}")


# list_serial_num()

# Реализуйте алгоритм перемешивания списка.
# НЕ ИСПОЛЬЗОВАТЬ ВСТРОЕННЫЕ БИБЛИОТЕКИ SHUFFLE,
# максимум использование библиотеки Random для и получения случайного int


def shuffle_list_wo_lib():
    my_list = ["one", 2, 3, 4, 5, 6, 7, 8, 9, "ten", 11, 12, 13, 14, 15]
    print(my_list)
    for i in range(len(my_list)):
        random_int = int(
            len(my_list)*((time.clock_gettime_ns(time.CLOCK_MONOTONIC_RAW) % 100/100)))
        my_list.insert(random_int, my_list.pop(i))
    print(my_list)


shuffle_list_wo_lib()
