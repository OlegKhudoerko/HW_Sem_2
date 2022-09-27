#   1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
#   in -> out
#   - 6782 -> 23
#   - 0.67 -> 13
#   - 198.45 -> 27

#from unicodedata import decimal

#-----------Вариант 2---(обход float)
num = input("Введите любое вещественное число => ")
sum = 0

for i in range(len(num)):
    if num[i] != '.':
        sum+=int(num[i])
print(f'{num} -> {sum}')
