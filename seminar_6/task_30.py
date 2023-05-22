#Задача 30: Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
#Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
#Каждое число вводится с новой строки.

def arithmetic_progression(a1: int, n: int, d: int) -> list:
    list_arit_prog = []
    for i in range(1, n + 1):
        list_arit_prog.append(a1 + (i - 1) * d)
    return list_arit_prog

a1 = int(input("Введите первый элемент -> "))
n = int(input("Введите количество элементов -> "))
d = int(input("Введите разность элементов -> "))

print(arithmetic_progression(a1, n, d))