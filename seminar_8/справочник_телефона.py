# Задача №49. Решение в группах
# Создать телефонный справочник с
# возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер
# телефона - данные, которые должны находиться
# в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в
# текстовом файле
# 3. Пользователь может ввести одну из
# характеристик для поиска определенной
# записи(Например имя или фамилию
# человека)
# 4. Использование функций. Ваша программа
# не должна быть линейной
# same

import json

#phone_book = {
#     'Миша гараж':{'phone': ['72443351195','72627397543'] , 'birthday': '11-02-2010', 'email':"mail@mail.ru"},
#     'Sasha':{'phone': ['78436840045','77554802591']}}
phone_book = {}
db_path = 'phone_book.json'
def print_book(book):
    for k,v in book.items():
        print (k," - ", end = " | ")
        for i,j in v.items():
            print (i, j, end = " | ")
        print()

def save_db(path, db):
     with open(path, 'w', encoding='utf-8') as fh:  # открываем файл на запись
         fh.write(json.dumps(db, ensure_ascii=False))  # преобразовываем словарь data в unicode-строку и записываем в файл
         print('БД успещно сохранена')

def load_db(path):
     # загрузить из json
     with open(path, 'w', encoding='utf-8') as fh:  # открываем файл на чтение
         BD_local = json.load(fh)  # загружаем из файла данные в словарь data
     print('БД успещно загружена')
     return BD_local

def delete_book(phone_book):
    name = input("Введите пользователя, которого вы хотите удалить: ")
    if name in phone_book:
        del phone_book[name]
    else:
        print("Таким с именем человека нет")

def print_person (phone_book):
    name = input("Введите пользователя, которого вы хотите посмотреть: ")
    if name in load_db(phone_book):
        print(phone_book[name])
    else:
        print("Таким с именем человека нет")

def new_record(book):
     k=input("Put new name ")
     a={}
     a['phone']=list(input('put phone ').split())
     a['birthday']=input('put birthday ')
     a['email']=input('put email ')
     phone_book[k] = a
     book[k]=a

print("""выберите действие:
1. открыть базу данных
2. Добавить пользователя
3. Показать имя базы данных
4. Удалить пользователя
5. Показать пользователя
6. Выход из программы
""")
action = int(input("Введите номер задачи -> "))
while action != 6:
    if action == 1:
         print_book(phone_book)
    elif action == 2:
         new_record(phone_book)
    elif action == 3:
         print(db_path)
    elif action == 4:
         delete_book(phone_book)
    elif action == 5:
         print_person(phone_book)

    print("""выберите действие:
    1. открыть базу данных
    2. Добавить пользователя
    3. Показать имя базы данных
    4. Удалить пользователя
    5. Показать пользователя
    6. Выход из программы
    """)
    action = int(input("Введите номер задачи -> "))
save_db(db_path, phone_book)


