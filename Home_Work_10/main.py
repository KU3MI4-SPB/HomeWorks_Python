from manager import ContactsManager

path = 'Home_Work_10\contacts.csv'
contacts_manager = ContactsManager(path)

def main_menu():
    menu = '''
        Главное меню:
        1. Показать контакты
        2. Создать контакт
        3. Найти контакт
        4. Изменить контакт
        5. Удалить контакт
        6. Выход
    '''
    print(menu)

while True:
    main_menu()
    print()
    choice = input("Выберите пункт меню: ")

    if choice == '1':
        contacts_manager.show_contacts()
    elif choice == '2':
        contacts_manager.create_contact()
    elif choice == '3':
        contacts_manager.find_contact()
    elif choice == '4':
        contacts_manager.update_contact()
    elif choice == '5':
        contacts_manager.delete_contact()
    elif choice == '6':
        break
    else:
        print("Некорректный выбор пункта меню")
        print()

print()
print("До свидания! Программа завершена")