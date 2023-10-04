'''
Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt.
Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
1. Программа должна выводить данные
2. Программа должна сохранять данные в текстовом файле
3. Пользователь может ввести одну из характеристик для поиска определенной записи
   (например имя или фамилию человека)
4. Использование функций. Ваша программа не должна быть линейной

Дополнить телефонный справочник возможностью изменения и удаления данных.
Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал
для изменения и удаления данных.

'''
import csv
import os

# Функция для проверки существования файла и его создания, если он не существует
def create_file():
    if not os.path.isfile('phone.csv'):
        with open('phone.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Фамилия', 'Имя', 'Отчество', 'Номер телефона'])

# Функция для добавления новой записи
def add_rec():
    surname = input('Введите фамилию: ')
    name = input('Введите имя: ')
    fname = input('Введите отчество: ')
    tel = input('Введите номер телефона: ')

    with open('phone.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([surname, name, fname, tel])
    print('Запись добавлена успешно!')

# Функция для вывода всех записей
def show_all_rec():
    with open('phone.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(f'Фамилия: {row[0]}, Имя: {row[1]}, Отчество: {row[2]}, Номер телефона: {row[3]}')

# Функция для поиска записей по заданному критерию
def find_rec(attribut):
    with open('phone.csv', 'r') as file:
        reader = csv.reader(file)
        finding_recs = []
        for row in reader:
            if attribut in row:
                finding_recs.append(row)
        if finding_recs:
            print('Найденные записи:')
            for info in finding_recs:
                print(f'Фамилия: {info[0]}, Имя: {info[1]}, Отчество: {info[2]}, Номер телефона: {info[3]}')
        else:
            print('Записи не найдены.')

# Функция для изменения записи по имени или фамилии
def change_record(attribut):
    with open('phone.csv', 'r') as file:
        reader = csv.reader(file)
        data = list(reader)

    change_data = []
    for record in data:
        if attribut in record:
            new_surname = input(f'Введите новую фамилию для {record[0]}: ')
            new_name = input(f'Введите новое имя для {record[0]}: ')
            new_fname = input(f'Введите новое отчество для {record[0]}: ')
            new_tel = input(f'Введите новый номер телефона для {record[0]}: ')
            changed_rec = [new_surname, new_name, new_fname, new_tel]
            change_data.append(changed_rec)
        else:
            change_data.append(record)

    with open('phone.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(change_data)
    print('Запись успешно изменена!')

# Функция для удаления записи по имени или фамилии
def del_record(attribute):
    with open('phone.csv', 'r') as file:
        reader = csv.reader(file)
        record = list(reader)

    new_record = [record for record in record if attribute not in record]

    with open('phone.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(new_record)
    print('Запись успешно удалена!')

# Основной цикл программы
if __name__ == '__main__':
    create_file()

    while True:
        print('\nМеню:')
        print('1. Добавить запись')
        print('2. Вывести все записи')
        print('3. Поиск по характеристике')
        print('4. Изменить запись')
        print('5. Удалить запись')
        print('6. Выйти из программы')
        
        vybor = input('Выберите опцию (1/2/3/4/5/6): ')

        if vybor == '1':
            add_rec()
        elif vybor == '2':
            show_all_rec()
        elif vybor == '3':
            criteriy = input('Введите характеристику для поиска: ')
            find_rec(criteriy)
        elif vybor == '4':
            criteriy = input('Введите имя или фамилию для изменения записи: ')
            change_record(criteriy)
        elif vybor == '5':
            criteriy = input('Введите имя или фамилию для удаления записи: ')
            del_record(criteriy)
        elif vybor == '6':
            break
        else:
            print('Неверный выбор. Пожалуйста, выберите опцию из меню.')
