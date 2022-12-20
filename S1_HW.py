# Каждое задание, для удобства, разделено на блоки и выделено в отдельные функции,
# под каждым таким блоком есть строка вызова соответствующей функции,
# для запуска которой необходимо её раскомментировать, у остальных заданий закомментировать

# =============================
# Methods. Здесь блок общих методов
def get_num(msg):
    while True:
        try:
            val = float(input(msg))
        except ValueError:
            print("Требуется число")
        else:
            return val

# =============================
# Здесь начинаются задания

# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и
# проверяет, является ли этот день выходным.


def get_weekend_by_weekday():
    while True:
        try:
            numDay = int(input("Ввести цифру дня недели: "))
            if not (0 < numDay < 8):
                raise Exception("В неделе только 7 дней")
        except ValueError:
            print("Ожидается число")
        except Exception as e:
            print(e)
        else:
            break
    print("Выходной" if numDay > 5 else "Будний")


get_weekend_by_weekday()


# __________________________
# Напишите программу для проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
def check_predicate(x, y, z):
    l = not (x or y or z)
    r = not x and not y and not z
    return l == r


def predicate():
    for x in [True, False]:
        for y in [True, False]:
            for z in [True, False]:
                print(check_predicate(x, y, z))

# predicate()


# __________________________
# Напишите программу, которая принимает на вход координаты точки(X и Y),
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка(или на какой оси она находится).
def quarter_by_point():
    x = get_num("Ввод X: ")
    y = get_num("Ввод Y: ")
    quart = 0

    if (x == 0 or y == 0):
        print(f"Точка находится на оси.")
    else:
        if (x > 0):
            if (y > 0):
                quart = 1
            else:
                quart = 2

        else:
            if (y > 0):
                quart = 4
            else:
                quart = 3

        print(f"Точка находится в {quart} четверти.")


# quarter_by_point()


# __________________________
# Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти(x и y)
def range_by_quarter():
    while True:
        try:
            q = int(input("Ввод четверти: "))
            if not (0 < q < 5):
                raise Exception(
                    "Четверть - это диапазон от 1 до 4. Введите четверть.")

        except ValueError:
            print("Введите номер четверти цифрой от 1 до 4")

        except Exception as e:
            print(e)
        else:
            break

    print(
        f"X от 0 до {'+' if q in [1,2] else '-'}∞\nY от 0 до {'+' if q in [1,4] else '-'}∞")


# range_by_quarter()


# __________________________
# Напишите программу, которая принимает на вход координаты двух точек и
# находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21
def distance_2d():
    a, b = {}, {}
    a['x'] = get_num("Ввод Ax: ")
    a['y'] = get_num("Ввод Ay: ")
    b['x'] = get_num("Ввод Bx: ")
    b['y'] = get_num("Ввод By: ")

    dist = ((a.get('x') - b.get('x')) ** 2 +
            (a.get('y') - b.get('y')) ** 2) ** 0.5

    print(f"Расстояние между A и B = {dist - dist % 0.01}")


# distance_2d()
