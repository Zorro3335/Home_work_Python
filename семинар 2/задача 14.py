# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
# 10 -> 1 2 4 8
flag = True
while flag:
    num = int(input("Введите число -> "))
    for i in range(num + 1):
        if 2**i <= num:
            print(2**i, end=' ')

    answer = input("\nВы хотите продолжить? Если да, введите 'да', иначе 'нет' -> ")
    if answer.lower() == 'да':
        flag = True
    else:
        flag = False