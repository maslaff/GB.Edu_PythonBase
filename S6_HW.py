import math

# Задайте список из нескольких чисел. Напишите программу, которая
# найдёт сумму элементов списка, стоящих на позиции с нечетным индексом.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12


def sum_element_of_index():
    num_list = [2, 3, 5, 9, 3]
    # print(f"{num_list} -> на нечётных позициях элементы", end=' ')
    # acc = 0
    # for i in range(1, len(num_list), 2):
    #     print(f"{' и ' if acc else ''}{num_list[i]}", end='')
    #     acc += num_list[i]
    # print(f", ответ: {acc}")

    acc = [i for k, i in enumerate(num_list) if k % 2]
    print(
        f"{num_list} -> на нечётных позициях элементы {', '.join(map(str, acc))}, ответ: {sum(acc)}")

# sum_element_of_index()
# ______________________________________________________________________

# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

# Ничего умнее не придумал, чем просто заниндзякодить в одну строку


def mul_numpare():
    # num_list = [2, 3, 5, 6]
    num_list = [2, 3, 4, 5, 6]

    # mul_list = []

    # for i in range(math.ceil(len(num_list)/2)): # Вариант с бибилиотекой math
    # for i in range(int(len(num_list)/2) + len(num_list) % 2):
    #     mul_list.append(num_list[i] * num_list[-i-1])

    print(
        f"{num_list} => {[num_list[i] * num_list[-i-1] for i in range(int(len(num_list)/2) + len(num_list) % 2)]}")


# mul_numpare()
# ______________________________________________________________________


# Задайте список из вещественных чисел. Напишите программу, которая
# найдёт разницу между максимальным и минимальным значением дробной части элементов, отличной от 0.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19
def dif_minmax_fract(num_list):
    # nl = [int(i*100 % 100) for i in num_list]
    # print(min(nl), max(nl))
    # nmin = nl[0]
    # nmax = nl[0]
    # for i in nl:
    #     if i:
    #         if i < nmin:
    #             nmin = i
    #         elif i > nmax:
    #             nmax = i
    # print(f"{num_list} => {(nmax-nmin)/100}")

    # nl = [float('.' + str(i).split('.')[1]) for i in num_list if i % 1]
    nl = [float(str(i)[str(i).rindex('.'):]) for i in num_list if i % 1]
    print(f"{num_list} => {max(nl) - min(nl)}")


# dif_minmax_fract([1.1, 1.2, 3.1, 5, 10.01])
# ______________________________________________________________________


# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10

def dec_to_bin(n):
    # a = ''
    # n = nm
    # while n:
    #     a = str(n % 2) + a
    #     n //= 2

    # print(f"{nm} -> {a}")

    print(
        f"{n} -> {''.join(reversed([str([n%2, n:=n//2][0]) for _ in range(8*(n//255+1))]))}")


dec_to_bin(45)
# ______________________________________________________________________

# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] Негафибоначчи

# Твой ниндзя-код подшаманил и вуаля..


def negafibonacci(k):
    # if k < 1:
    #     print('[0]')
    #     return

    # f = [1, 0, 1]

    # for i in range(k-1):
    #     f.append(f[-2] + f[-1])
    #     f.insert(0, f[1] - f[0])

    # print(f)

    print((x := [1, 0, 1], [(x.insert(0, x[1]-x[0]),
          x.append(x[-1]+x[-2])) for _ in range(k-1)])[0])


# negafibonacci(8)
# ______________________________________________________________________
