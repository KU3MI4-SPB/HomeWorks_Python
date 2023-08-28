# Задача 18: Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai
# . Последняя строка
# содержит число X

import random

n = int(input('Введите количество элементов массива: '))
list_1 = [random.randint(1, 99) for i in range(n)]

x = int(input('Введите число X от 1 до 99: '))

find_num = list_1[0]
diff = abs(x - list_1[0])

for i in range(1,n):
    current_diff = abs(x - list_1[i])
    if current_diff < diff:
        find_num = list_1[i]
        diff = current_diff

print('Полученный массив: ', list_1)
print('Самый близкий по величине элемент к числу', x, 'является:', find_num)