import json


class PhoneBookApp:
    def __init__(self):
        self.data = self.load_data('data.json')
        self.entries = self.data['Guide']

    def save_data(self, data, filename):  # сохраняет переданные данные в формате JSON в указанный файл
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    def load_data(self, filename):  # загружает данные из указанного JSON-файла
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                return json.load(file)
        except FileNotFoundError:
            return {"Guide": {}}

    def add_entry(self, input_function=input):  # добавляет новую запись в телефонную книгу
        new_entry = {}
        new_entry['фамилия'] = input_function("Введите фамилию: ")
        new_entry['имя'] = input_function("Введите имя: ")
        new_entry['отчество'] = input_function("Введите отчество: ")
        new_entry['организация'] = input_function("Введите название организации: ")
        new_entry['телефон рабочий'] = input_function("Введите рабочий телефон: ")
        new_entry['телефон личный'] = input_function("Введите личный телефон: ")

        next_index = str(len(self.entries) + 1)
        self.entries[next_index] = new_entry
        self.save_data(self.data, 'data.json')

    def list_entries(self):  # выводит на экран список всех записей
        entries = self.entries
        if not entries:
            print("Справочник пуст.")
            return
        for index, entry in entries.items():
            print(f"Запись {index}:")
            print(f"  Фамилия: {entry['фамилия']}")
            print(f"  Имя: {entry['имя']}")
            print(f"  Отчество: {entry['отчество']}")
            print(f"  Организация: {entry['организация']}")
            print(f"  Телефон рабочий: {entry['телефон рабочий']}")
            print(f"  Телефон личный: {entry['телефон личный']}")
            print("-" * 30)

    def edit_entry(self):  # позволяет пользователю выбрать запись и изменить её данные
        self.list_entries()
        entry_number = input("Введите номер записи, которую хотите отредактировать: ")

        if entry_number in self.entries:
            entry = self.entries[entry_number]
            print(f"Редактирование записи {entry_number}:")
            entry['фамилия'] = input("Введите фамилию: ")
            entry['имя'] = input("Введите имя: ")
            entry['отчество'] = input("Введите отчество: ")
            entry['организация'] = input("Введите название организации: ")
            entry['телефон рабочий'] = input("Введите рабочий телефон: ")
            entry['телефон личный'] = input("Введите личный телефон: ")
            self.save_data(self.data, 'data.json')
            print("Запись успешно отредактирована.")
        else:
            print("Некорректный номер записи.")

    def search_entries(self, search_query1, search_query2=None):  # поиск записей в телефонной книге
        results = {}
        for index, entry in self.entries.items():
            if search_query2:
                match1 = any((search_query1.lower() in value.lower()) for value in entry.values())
                match2 = any((search_query2.lower() in value.lower()) for value in entry.values())
                if match1 or match2:
                    results[index] = entry
            else:
                match = any((search_query1.lower() in value.lower()) for value in entry.values())
                if match:
                    results[index] = entry
        return results

    def main(self):  # меню
        while True:
            print("\nМеню:")
            print("1. Вывести записи")
            print("2. Добавить запись")
            print("3. Редактировать запись")
            print("4. Поиск записей")
            print("5. Выйти")

            choice = input("Выберите действие: ")

            if choice == '1':
                self.list_entries()
            elif choice == '2':
                self.add_entry()
            elif choice == '3':
                self.edit_entry()
            elif choice == '4':
                search_query1 = input("Введите первый параметр для поиска: ")
                search_query2 = input("Введите второй параметр для поиска: ")
                search_results = self.search_entries(search_query1, search_query2)
                if not search_results:
                    print("Ничего не найдено.")
                else:
                    print("Результаты поиска:")
                    for index, entry in search_results.items():
                        entry_text = f"Запись {index}:\n" + \
                                     f"  Фамилия: {entry['фамилия']}\n" + \
                                     f"  Имя: {entry['имя']}\n" + \
                                     f"  Отчество: {entry['отчество']}\n" + \
                                     f"  Организация: {entry['организация']}\n" + \
                                     f"  Телефон рабочий: {entry['телефон рабочий']}\n" + \
                                     f"  Телефон личный: {entry['телефон личный']}\n" + \
                                     "-" * 30
                        print(entry_text)
            elif choice == '5':
                print("Программа завершена.")
                break
            else:
                print("Некорректный выбор. Попробуйте еще раз.")

            self.data['Guide'] = self.entries
            self.save_data(self.data, 'data.json')


if __name__ == "__main__":
    app = PhoneBookApp()
    app.main()
