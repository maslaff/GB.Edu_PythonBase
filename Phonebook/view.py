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


def main_menu():
    commands = ['Показать все контакты',
                'Открыть файл',
                'Сохранить файл',
                'Новый контакт',
                'Изменить контакт',
                'Удалить контакт',
                'Найти контакт',
                'Выйти из программы']
    print('Выберите пункт меню: ')
    for i in range(len(commands)):
        print(f"\t{i+1}. {commands[i]}")
    return get_num('\nВведите пункт меню: ', len(commands))


def show_contacts(phonebook: list):
    if len(phonebook):
        for i, it in enumerate(phonebook):
            print(f" {i+1}) {it[0]} - {it[1]} ({it[2]})")
    else:
        print('Пусто')


def load_succes():
    print('Телефонная книга загружена')


def save_succes():
    print('Телефонная книга сохранена')


def new_contact():
    new = []
    name = input('Введите Имя Фамилию: ').capitalize()
    number = input('Введите номер: ')
    comment = input('Введите комментарий: ')

    return name, number, comment


def find_contact():
    return input('Введите запрос: ')


def edit_contact(phonebook: list):
    print('Изменить контакт:')
    show_contacts(phonebook)
    contact = get_num('Выберите контакт: ', len(phonebook))
    print('  1)  Имя Фамилия\n  2)  Номер телефона\n   3) Комментарий')
    field = get_num('Введите поле для изменения: ', 3)
    value = input('Введите новое значение: ')
    return contact-1, field-1, value


def delete_contact(phonebook: list):
    show_contacts(phonebook)
    return get_num('Введите номер контакта: ', len(phonebook))
