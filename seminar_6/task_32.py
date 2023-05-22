#Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)


def list_1(length_list: int) -> list:
	list_2 = list()
	for i in range(length_list):
		list_2.append(int(input(f"Введите {i + 1} элемент массива -> ")))
	return list_2

def result_list(list1: list, min_dia: int, max_dia: int) -> list:
	list_result = list()
	for i in range(len(list1)):
		if min_dia <= list1[i] <= max_dia:
			list_result.append(i)
	return list_result
length_list = int(input("Введите длину списка ->") )
random_list = list_1(length_list)
min_dia = int(input("Введите минимальное число диапазона -> "))
max_dia = int(input("Введите максимальное число диапазона -> "))
print(result_list(random_list, min_dia, max_dia))