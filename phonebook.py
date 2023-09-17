class PhoneBook:
    def display_contacts(self):
        with open('phonebook.txt', 'r') as file:
            for line in file:
                name, number = line.strip().split(',')
                print(f'Имя: {name}, Номер: {number}')

    def add_contact(self, name, number):
        with open('phonebook.txt', 'a') as file:
            file.write(f'{name},{number}\n')

    def search_contact(self, query):
        with open('phonebook.txt', 'r') as file:
            for line in file:
                name, number = line.strip().split(',')
                if query in name:
                    print(f'Имя: {name}, Номер: {number}')

    def delete_contact(self, query):
        contacts = []
        with open('phonebook.txt', 'r') as file:
            for line in file:
                contact_name, contact_number = line.strip().split(',')
                if contact_name != query:
                    contacts.append(line)

        with open('phonebook.txt', 'w') as file:
            file.writelines(contacts)

    def update_contact(self, name, new_number):
        contacts = []
        with open('phonebook.txt', 'r') as file:
            for line in file:
                contact_name, contact_number = line.strip().split(',')
                if contact_name == name:
                    line = f'{contact_name},{new_number}\n'
                contacts.append(line)

        with open('phonebook.txt', 'w') as file:
            file.writelines(contacts)


phonebook = PhoneBook()

while True:
    print("Меню:")
    print("1. Просмотреть контакты")
    print("2. Добавить контакт")
    print("3. Искать контакт")
    print("4. Удалить контакт")
    print("5. Обновить номер телефона")
    print("6. Выход")

    choice = input("Выберите действие (1/2/3/4/5/6): ")

    if choice == '1':
        phonebook.display_contacts()
    elif choice == '2':
        name = input("Введите название контакта: ")
        number = input("Введите номер телефона: ")
        phonebook.add_contact(name, number)
    elif choice == '3':
        query = input("Введите имя для поиска: ")
        phonebook.search_contact(query)
    elif choice == '4':
        query = input("Введите имя для удаления: ")
        phonebook.delete_contact(query)
    elif choice == '5':
        name = input("Введите имя контакта для обновления: ")
        new_number = input("Введите новый номер телефона: ")
        phonebook.update_contact(name, new_number)
    elif choice == '6':
        break
    else:
        print("Ошибка. Попробуйте еще раз")