#каждой фразе стихотворения одинаковое. Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг от
#друга пробелами. Стихотворение Винни-Пух вбивает в программу с клавиатуры. В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с
#ритмом все не в порядке

#Ввод:

#пара-ра-рам рам-пам-папам па-ра-па-дам

#Вывод:

#Парам пам-пам

def param_pam_pam(massege: str) -> str:
    dict1 = dict()
    flag = True
    massege = massege.lower().split()
    key_num = 0
    vowels = set("аоеиюэяуыё")
    for i in massege:
        count = 0
        for j in i:
            if j in vowels:
                dict1[key_num] = count + 1
                count += 1
        key_num += 1

    for i in range(len(dict1) - 1):
        if dict1[i + 1] == dict1[i]:
            flag = True
        else:
            return "Пам парам"
    if flag:
        return "Парам пам-пам"
print(param_pam_pam(input("Введите кричалку Винни-Пуха -> ")))