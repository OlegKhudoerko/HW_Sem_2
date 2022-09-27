# * 4. Напишите программу, которая принимает на вход 2 числа.
# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях(не индексах).
# Position one: 1
# Position two: 3
# Number of elements: 5
# -> [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
# -> 15

a = int(input('Введите число 1 позиции => '))
b = int(input('Введите число 2 позиции => '))
n = int(input('Введите число для списка => '))
if 0 > a or a > n or 0 > b or b > n:
    print('Некорректный ввод!')
else:
    data = []
    for i in range(-n, n+1):
        data.append(i)
    print(
        f'Position one: {a} \nPosition one: {b} \nNumber of elements: {n} \n-> {data}')
    print(f'-> {(data[a-1]*data[b-1])}')
