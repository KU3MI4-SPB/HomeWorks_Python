import csv
from contact import Contact

class ContactsManager:
    def __init__(self, path):
        self.path = path

    def show_contacts(self):
        with open(self.path, mode='r', encoding='UTF-8') as file:
            reader = csv.reader(file)
            for row in reader:
                contact = Contact(row[0], row[1], row[2])
                print(contact)
            print()

    def create_contact(self):
        name = input("Введите Имя: ")
        email = input("Введите почту: ")
        phone = input("Введите телефон: ")

        contact = Contact(name, email, phone)
        with open(self.path, mode='a', encoding='UTF-8', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([contact.name, contact.email, contact.phone])
        print('Контакт успешно добавлен')
        print()

    def find_contact(self):
        search_term = input("Введите имя для поиска: ")
        with open(self.path, mode='r', encoding='UTF-8') as file:
            reader = csv.reader(file)
            for row in reader:
                if search_term.lower() in row[0].lower():
                    contact = Contact(row[0], row[1], row[2])
                    print(contact)
                    print()
                    break
            else:
                print("Контакт не найден")
                print()

    def update_contact(self):
        search_term = input("Введите имя контакта для изменения: ")
        with open(self.path, mode='r', encoding='UTF-8') as file:
            contacts = list(csv.reader(file))
            for i, row in enumerate(contacts):
                if search_term.lower() in row[0].lower():
                    name = input("Введите новое имя: ")
                    email = input("Введите новую почту: ")
                    phone = input("Введите новый телефон: ")
                    contacts[i] = [name, email, phone]
                    break
            else:
                print("Контакт не найден")
                print()

        with open(self.path, mode='w', encoding='UTF-8', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(contacts)
        print('Контакт успешно изменен')
        print()

    def delete_contact(self):
        search_term = input("Введите имя контакта для удаления: ")
        with open(self.path, mode='r', encoding='UTF-8') as file:
            contacts = list(csv.reader(file))
            for row in contacts:
                if search_term.lower() in row[0].lower():
                    contacts.remove(row)
                    break
            else:
                print("Контакт не найден")
                print()

        with open(self.path, mode='w', encoding='UTF-8', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(contacts)
        print('Контакт успешно удален')
        print()