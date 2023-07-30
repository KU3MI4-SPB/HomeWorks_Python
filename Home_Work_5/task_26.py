# Задача 26: Напишите программу, которая на вход принимает
# два числа A и B, и возводит число А в целую степень B с
# помощью рекурсии

def abc(a, b):
    if b == 0:
        return 1
    else:
        return a * abc(a, b - 1)
    
num_a = int(input('Введите число A: '))
num_b = int(input('Введите число B: '))

result = abc(num_a, num_b)

print(f'Число {num_a} в степени числа {num_b}, равняется: {result}')