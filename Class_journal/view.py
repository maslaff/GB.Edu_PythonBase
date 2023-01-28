import os


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


def choose_class(class_list):
    clear()
    # print("   0) Ввести...")
    print('\n'.join([f"   {k+1}) {i.upper()}" for k,
          i in enumerate(class_list)]))
    choice = get_num('Выберите класс: ', len(class_list))-1
    # if choice == -1:

    return class_list[choice]


# def input_new_class():
#     while True:
#         inp = input("Введите название добавляемого класса: ").lower()[:2]
#         if len(inp) == 2 and inp[0].isdigit() and inp[1].isalpha:
#             return inp


def choose_subj(subj_list: list):
    clear()
    print('\n'.join([f"   {k+1}) {i.capitalize()}" for k,
          i in enumerate(subj_list)]))
    return get_num('Выберите предмет: ', len(subj_list))-1


def print_head(cl: str, subj: str):
    clear()
    print(f"Класс: {cl.upper()}\n{subj.capitalize()}")


def choose_student(journal):
    print("   0) exit")
    print('\n'.join([f"   {k+1}) {i.capitalize()}: {', '.join(journal[i])}" for k,
          i in enumerate(journal)]))
    return get_num('Выберите кто пойдет к доске: ', len(journal), 0)-1


def choose_eval():
    return get_num('Оценка: ', 5)


def goodbye():
    print('Хорошего дня!')
