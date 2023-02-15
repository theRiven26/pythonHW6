# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)
from random import randint
min = int(input("min = "))
max = int(input("max = "))
_list = [randint(1, 20) for i in range(int(input("Введите длину массива: ")))]
print(*_list)
newList = []
for i in range(len(_list)):
	if _list[i] > min and _list[i] < max:
		newList.append(i)
print(*newList)