path = 'Class_journal/3a.txt'
journal = {}


def open_journal():
    global path
    global journal

    with open(path, 'r') as f:
        input = f.readlines()
        for i in input:
            predm = i[:i.index(':')]
            chlds = {j.split(':')[0]: j.split(':')[1].strip().split(',')
                     for j in i[i.index(':')+1:].split(';')}
            journal[predm] = chlds


open_journal()
print(journal)
