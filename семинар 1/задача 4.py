# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов.
# Сколько журавликов сделал каждый ребенок, если известно,
# что Петя и Сережа сделали одинаковое количество журавликов, а
# Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# 6 -> 1 4 1
# 24 -> 4 16 4
# 60 -> 10 40 10

flag = True
while flag:
    s = int(input("Введите число -> "))
    print((s // 3) // 2, s - (s // 3), (s // 3) // 2)
    answer = input("Вы хотите продолжить? Если да, введите 'да', иначе 'нет' -> ")
    if answer.lower() == 'да':
        flag = True
    else:
        flag = False