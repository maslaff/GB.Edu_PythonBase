import os

journal = {}
path = ''
wd = 'Class_journal/classgroups'


def get_classes():
    classes = os.listdir(wd)
    return [i.split('.')[0] for i in classes]


def open_journal(cl):
    global path
    global journal
    global wd

    path = f"{wd}/{cl}.txt"

    with open(path, 'r') as f:
        input = f.readlines()
        for i in input:
            if '>' not in i:
                continue
            subj, data = i.strip().split('>')
            data = {i.split(':')[0]: i.split(':')[1].split(',')
                    for i in data.split(';')}
            journal[subj] = data


def get_journal():
    return journal


def save_journal(journal):
    global path
    data = []

    for k, i in journal.items():
        stud_evals = ';'.join(
            [f"{st}:{','.join(evals)}" for st, evals in i.items()])
        subj_string = f"{k}>{stud_evals}"
        data.append(subj_string)

    with open(path, 'w') as f:
        f.write('\n'.join(data))
