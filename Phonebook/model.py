phonebook = []
path = 'Phonebook/phonebook.txt'


def open_phonebook():
    global phonebook
    global path
    with open(path, 'r') as f:
        data = f.readlines()
        for ln in data:
            phonebook.append(ln.strip().split(';'))


def save_phonebook():
    global phonebook
    global path
    data = []
    for ln in phonebook:
        data.append(';'.join(ln))
    with open(path, 'w') as f:
        data = f.write('\n'.join(data))


def update_phonebook(contact: list):
    global phonebook
    phonebook.append(contact)


def get_phonebook():
    global phonebook
    return phonebook


def search_contact(search: str):
    global phonebook
    search_res = []
    for ln in phonebook:
        for field in ln:
            if search in field:
                search_res.append(ln)
                break
    return search_res


def update_contact(contact, field, new_value):
    phonebook[contact][field] = new_value
