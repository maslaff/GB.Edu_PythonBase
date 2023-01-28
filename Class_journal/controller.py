import model
import view

classgroup = ''
subj = ''


def start_session():
    global classgroup
    classgroup = view.choose_class(model.get_classes())
    model.open_journal(classgroup)
    session(model.get_journal())


def session(journal):
    global classgroup
    global subj
    subj = list(journal)[view.choose_subj(list(journal))]
    while True:
        view.print_head(classgroup, subj)
        student = view.choose_student(journal[subj])
        if student == -1:
            view.goodbye()
            break
        student = list(journal[subj])[student]
        eval = view.choose_eval()
        print(journal)
        journal[subj][student].append(str(eval))

    model.save_journal(journal)
