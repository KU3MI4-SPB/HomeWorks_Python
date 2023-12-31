# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх
# решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.

import random

n = int(input('Введите количество монеток: '))

heads = 0
tails = 0

for i in range(n):
    coin = random.randint(0, 1)
    if coin == 0:
        tails += 1
    elif coin == 1:
        heads += 1    
    print(coin, end=' ')
print('- выпали такие монетки')

min_flips = min(heads, tails)
print()
print('Минимальное количество монеток, которые нужно перевернуть:', min_flips)