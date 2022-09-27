# 3. Задайте список из n чисел, заполненный
#    по формуле (1 + 1/n) ** n и выведите на экран их сумму.
#    Для n = 6: [2, 2, 2, 2, 2, 3] -> 13

num = int(input('Введите число => '))

data = []
sum = 0

for i in range(1, num+1):
    data.append(round((1+1/i)**i))
    sum += data[i-1]

print(f"Для n = {num}: {data} -> {sum:.0f}")
