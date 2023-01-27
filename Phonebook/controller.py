import model
import view


def start_session():
    user_choice = 0
    while user_choice != 8:
        user_choice = view.main_menu()

        match user_choice:
            case 1:
                view.show_contacts(model.get_phonebook())
            case 2:
                model.open_phonebook()
                view.load_succes()
            case 3:
                model.save_phonebook()
                view.save_succes()
            case 4:
                model.update_phonebook(list(view.new_contact()))
            case 5:
                model.update_contact(*view.edit_contact(model.get_phonebook()))
            case 6:
                model.remove_contact(
                    view.delete_contact(model.get_phonebook()))
            case 7:
                view.show_contacts(model.search_contact(view.find_contact()))
