# =============================
# Methods. Здесь блок общих методов
import time
import os
from random import randint as rnd


def get_num(msg, max=999, min=1):
    while True:
        try:
            val = int(input(msg))
            if val < min:
                print(f"Число не должно быть меньше {min}")
                continue
            if val > max:
                print(f"Число не должно быть больше {max}")
                continue
        except ValueError:
            print("Требуется число")
        else:
            return val


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# =============================

# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит заданное количество конфет.
# Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# a) Добавьте игру против бота
# b) Подумайте как наделить бота 'интеллектом'


def postfix_match(num):
    while num > 99:
        num %= 100
    # if num == 0 or (num > 4 and num < 20):
    if 10 < num < 20:
        return ''
    num %= 10
    if num == 0 or num > 4:
        return ''
    if num == 1:
        return 'у'
    else:
        return 'ы'


def print_brief(swts, p_swts, cnt):
    clear()
    print(f"На столе {swts} конфет{postfix_match(swts)}")
    print(f"На шаге {cnt} взяли:")
    print(
        f"{p_swts[1]['name']}: {p_swts[1]['cnt']} конфет{postfix_match(p_swts[1]['cnt'])}")
    print(
        f"{p_swts[2]['name']}: {p_swts[2]['cnt']} конфет{postfix_match(p_swts[2]['cnt'])}")


def sweets():
    MAX_BET = 28
    clear()
    SWTS = get_num("Введите начальное число конфет на столе: ")
    swts = SWTS
    player_order = [1, 2]
    current_player = rnd(0, 1)
    if current_player:
        player_order = [2, 1]
    current_player = current_player+1
    count = 0

    player = {1: {'cnt': 0, 'name': ''}, 2: {'cnt': 0, 'name': 'Ботя'}}
    bot_mode = bool(input(
        "Будете ли вы играть с ботом или человеком?\nВведите 1 если хотите играть с ботом или Enter для игры вдвоем: "))
    player[1]['name'] = input(
        f"Введите имя {'' if bot_mode else 'первого '}игрока: ")

    if not bot_mode:
        player[2]['name'] = input(f"Введите имя второго игрока: ")

    print_brief(swts, player, count)
    print(f"Первым будет ходить {player[current_player]['name']}")
    input('[ Нажмите Enter ]')
    print_brief(swts, player, count)

    while swts > 0:
        count += 1
        for pl in player_order:
            current_player = pl
            if bot_mode and pl == 2:
                if swts <= MAX_BET:
                    n = swts
                elif swts >= MAX_BET*2+1:  # 57
                    n = MAX_BET

                else:
                    n = swts - (MAX_BET+1)  # !!! Может вернуть 0!

            else:
                print(
                    f"Введите количество конфет, которое желаете взять (не более {MAX_BET if swts >= MAX_BET else swts})")
                n = get_num(f"{player[pl]['name']}: ", MAX_BET)
                if n > swts:
                    n = swts
            swts -= n
            player[pl]['cnt'] = n
            if swts <= 0:
                break
            print_brief(swts, player, count)

    print_brief(swts, player, count)
    print(f"Победил {player[current_player]['name']}. Поздравляем!")
    print("\n O O\nO O O\n \\|/\n  *\n  |\n")
    print(f"{' '.join(list(player[current_player]['name'].upper()))}")


# sweets()

# Создайте программу для игры в 'Крестики-нолики'
# НЕОБЯЗАТЕЛЬНО Добавить игру против бота с интеллектом

player = ['x', 'o']


def print_field(field):
    print("    1   2   3")
    print('   ' + '-'*11)
    for n, i in enumerate(field):
        print(f"{n+1} |", end='')
        for j in i:
            print(f" {j}", end=' |')
        print()
        print('   ' + '-'*11)


def resolve(field):
    # diag = field + list(zip(*field)) + [[i[k] for k, i in enumerate(field)]] + [[
    #     i[-(k+1)] for k, i in enumerate(field)]]

    diag = field + \
        list(zip(*field)) + \
        [[field[i][i] for i in range(3)]] + \
        [[field[i][-(i+1)] for i in range(3)]]

    for i in diag:
        for p in player:
            if i.count(p) == 3:
                return p

    return False


def crosszero():
    field = [[' ', ' ', ' '],
             [' ', ' ', ' '],
             [' ', ' ', ' ']]
    pl = 0

    clear()
    print_field(field)
    for i in range(9):
        print(f'Ходит {player[pl]}')
        while True:
            turn = input('Ячейка: ').replace(' ', '')[:2]

            if len(turn) < 2 or not turn.isnumeric():
                print("Требуется два числа от 1 до 3")
                continue

            y, x = list(map(int, turn))

            if not field[y-1][x-1] == ' ':
                print('Ячейка занята. Выберите пустую')
                continue

            break

        field[y-1][x-1] = player[pl]

        pl = not pl
        clear()
        print_field(field)
        r = resolve(field)
        if r:
            print(f"Победил {r}")
            return
    print('Ничья!')


# crosszero()


# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# aaaaabbbcccc -> 5a3b4c
# 5a3b4c -> aaaaabbbcccc

def rle_pack(data: str):
    cnt = 1
    res = ''
    for i in range(len(data)-1):
        if data[i] == data[i+1]:
            cnt += 1
        else:
            res += str(cnt) + data[i]
            cnt = 1
    res += str(cnt) + data[-1]

    return res


def rle_unpack(data: str):
    num = ''
    res = ''

    for i in data:
        if i.isdecimal():
            num += i
        else:
            res += i*int(num)
            num = ''
    return res


def rle(data: str):
    if data.isalpha():
        return rle_pack(data)

    elif data[0].isdecimal():
        return rle_unpack(data)

    else:
        return "Неверный формат строки"


raw_file = 'raw_data'
conv_file = 'conv_data'


def rle_start():
    with open(raw_file, 'r') as fread, open(conv_file, 'w') as fwrite:
        fwrite.write('\n'.join(map(rle, [i.strip()
                     for i in fread.readlines()])))


# rle_start()
# _________________________________________________________________________
