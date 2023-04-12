# Задача 2: Найдите сумму цифр трехзначного числа.
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)


sumNumber = 0
flag = True
while flag:
    number = int(input("Введтие число -> "))
    if 100 <= number < 1000:
        while number != 0:
            sumNumber += number % 10
            number //= 10
        print(f'Сумма чисел в трехнзначном числе равно {sumNumber}')
        answer = input("Вы хотите еще раз попробывать? Если да, введите 'да' иначе 'нет' -> ")
        if answer == "да":
            flag = True
        else:
            flag = False

    else:
        print("Вы ввели не трехзначное число :(")
        answer = input("Вы хотите еще раз попробывать? Если да, введите 'да' иначе 'нет' -> ")
        if answer == "да":
            flag = True
        else:
            flag = False
