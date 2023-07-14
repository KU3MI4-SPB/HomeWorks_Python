# Найдите сумму цифр трехзначного числа. 

number = int(input('Введите трехзначное число: '))
if number > 100 and number < 1000:
    dig1 = number // 100
    dig2 = (number % 100) // 10
    dig3 = number % 10
    summa = dig1 + dig2 + dig3
else:
    print('Число не трехзначное')
print('Сумма чисел равна: ', summa)