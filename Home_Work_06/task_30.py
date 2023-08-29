# Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент, 
# разность и количество элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: 
# an = a1 + (n - 1) * d
# Каждое число вводится с новой строки

def a_progress(a1, d, n):
    progression = []
    for i in range(n):
        element = a1 + (i * d) 
        progression.append(element) 
    return progression

a1 = int(input('Введите первый элемент: '))
d = int(input('Введите разность: '))
n = int(input('Введите количество элементов: '))

result = a_progress(a1, d, n)
print(f'Получненный массив: {result}')