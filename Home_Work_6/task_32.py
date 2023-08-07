# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат 
# заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)

import random

def find_index(arr, min_val, max_val):
    index = []  
    for i in range(len(arr)):
        if min_val <= arr[i] <= max_val: 
            index.append(i)  
    return index

n = int(input('Введите размер массива: '))
min_val = int(input('Введите минимальное значение: '))
max_val = int(input('Введите максимальное значение: '))

arr = [random.randint(1, 50) for _ in range(n)] 

print('Исходный массив:', arr)

result = find_index(arr, min_val, max_val)

if result:
    print('Индексы элементов, удовлетворяющих условию:', result)
else:
    print('Нет элементов, удовлетворяющих условию')