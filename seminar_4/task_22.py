##Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются
# в обоих наборах.
###Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств.


def set_1(length_set: int) -> setset:
    set_2 = set()
    for i in range(length_set):
        set_2.add(int(input(f"Введите {i + 1} элемент множества -> ")))
    return set_2set_2


print(set_1(int(input("Введите длину 1 множества -> "))) & set_1(int(input("Введите длину 2 множества -> "))))
