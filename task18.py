# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент 
# к заданному числу X. Пользователь в первой строке вводит натуральное число N –
# количество элементов в массиве. В последующих  строках записаны N целых чисел Ai. 
# Последняя строка содержит число X
# *Пример:*

# 5
#     1 2 3 4 5
#     6
#     -> 5
from random import randint
list = []
listRange = int(input('Введите длину массива:'))
for i in range (listRange):
    list.append(randint(1,100))
print(*list)
num = int(input('Введите число:'))
NumInList = 0
diff = 1000
for i in range (listRange):
    if num < list[i]:
        if list[i]-num < diff:
            diff = list[i]-num
            NumInList = list[i]
    else:
        if num - list[i] < diff:
            diff = num - list[i]
            NumInList = list[i]
print(f'Элемент массива, самый близкий по величине к числу {num} - {NumInList} ')
            